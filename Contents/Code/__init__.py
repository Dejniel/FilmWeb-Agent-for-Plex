def Start():
    Log("FilmWebStandaloneAgent is starting up.")
    
from difflib import SequenceMatcher

# Agent FilmWebStandaloneAgent
class FilmWebStandaloneAgent(Agent.Movies):
    name = 'FilmWeb.pl'
    languages = ['pl']  # Zastąpienie Locale.Language.Polish uproszczonym podejściem
    accepts_from = ['com.plexapp.agents.localmedia']
    BASE_URL = "https://www.filmweb.pl/api/v1"
    SEARCH_URL = BASE_URL + "/live/search?query=%s&pageSize=12"
    FILM_INFO_URL = BASE_URL + "/title/%s/info"
    DESCRIPTION_URL = BASE_URL + "/film/%s/description"
    RATING_URL = BASE_URL + "/film/%s/rating"
    CRITICS_RATING_URL = BASE_URL + "/film/%s/critics/rating"
    PREVIEW_URL = BASE_URL + "/film/%s/preview"

    def get_api(self, url):
        headers = {'x-locale': 'pl_PL'}
        try:
            response = JSON.ObjectFromURL(url, headers=headers)
            if response:
                Log("API response received from %s" % url)
                return response
        except Exception as e:
            Log("API request error: %s" % e)
        return None
    def quote(self, s):
        safe = "/:"  # Zdefiniuj, które znaki uważasz za bezpieczne
        result = []
        for char in list(s):  # Zmień string na listę, aby wymusić iterację
            if char.isalnum() or char in safe:
                result.append(char)
            else:
                result.append('%{0:02X}'.format(ord(char)))
        return ''.join(result)
    def search(self, results, media, lang):
        query = media.name
        if media.year:
            query += " %s" % media.year
        query = self.quote(query)
        
        # Wykonanie zapytania do API Filmweb w celu pobrania listy wyników
        Log("Performing search with query: %s" % query)
        search_response = self.get_api(self.SEARCH_URL % query)
        search_results = search_response.get("searchHits", []) if search_response else []

        if not search_results:
            Log.Info("No search results found.")
            return 1

        favorise_firsts_results = int(Prefs['favoriseFirstsResults'])
        order_num = 0

        for film_data in search_results:
            if film_data.get("type") in ["serial", "film"]:  # Dozwolone typy wyników
                # Pobranie dodatkowych informacji o filmie na podstawie jego ID
                Log("Fetching film info for ID: %s" % film_data['id'])
                film_info = self.get_api(self.FILM_INFO_URL % film_data['id'])
                Log("Fetching film: %s" % film_info)
                if film_info:
                    # Połączenie danych z wyszukiwania i dodatkowych informacji
                    film_data.update(film_info)

                    # Obliczanie wyniku podobieństwa (score)
                    score = self.calculate_score(media, film_data, favorise_firsts_results, order_num)

                    # Dodanie wyniku do listy wyników wyszukiwania Plex
                    results.Append(MetadataSearchResult(
                        id=str(film_data['id']),
                        name=film_data['title'],
                        year=film_data['year'],
                        score=score,
                        lang=lang
                    ))
                    Log("Added search result: %s with score %s" % (film_data['title'], score))

                    order_num += 1

    def calculate_score(self, media, film_data, favorise_firsts_results, order_num):
        year_penalty = 0
        if media.year:
            year_penalty = abs(int(media.year) - film_data['year'])
            if 'otherYear' in film_data:
                year_penalty = min(year_penalty, abs(int(media.year) - film_data['otherYear']))
            year_penalty = year_penalty * 4
        
        # Obliczanie podobieństwa tytułu przy użyciu SequenceMatcher
        similarity_score = SequenceMatcher(None, media.name.lower(), film_data['title'].lower()).ratio()
        if 'originalTitle' in film_data:
            similarity_score = max(similarity_score, SequenceMatcher(None, media.name.lower(), film_data['originalTitle'].lower()).ratio())
        similarity_score = similarity_score * 100
        return max(0, int(similarity_score) - year_penalty - (favorise_firsts_results * order_num))

    def set_metadata_value(self, metadata, key, value):
        if value and not getattr(metadata, key):
            setattr(metadata, key, value)
            Log("Set metadata %s to %s" % (key, value))

    def update(self, metadata, media, lang):
        # Dekodowanie ID
        #Log("Undecoded metadata ID: %s %s" % (metadata.id, metadata.title))
        metadata_id = metadata.id
        #Log("Decoded metadata ID: %s" % metadata_id)
      
        # Logo filmweb przy ocenie
        self.set_metadata_value(metadata, 'rating_image', R('filmweb_logo.png'))

        # Pobranie opisu
        description_data = self.get_api(self.DESCRIPTION_URL % metadata_id)
        if description_data:
            self.set_metadata_value(metadata, 'summary', description_data.get('synopsis'))

        # Pobranie oceny użytkowników
        rating_data = self.get_api(self.RATING_URL % metadata_id)
        if rating_data:
            self.set_metadata_value(metadata, 'audience_rating', rating_data.get('rate'))

        # Pobranie oceny krytyków
        critics_rating_data = self.get_api(self.CRITICS_RATING_URL % metadata_id)
        if critics_rating_data:
            self.set_metadata_value(metadata, 'rating', critics_rating_data.get('rate'))

        # Pobranie dodatkowych informacji z podglądu
        preview_data = self.get_api(self.PREVIEW_URL % metadata_id)
        if preview_data:
            self.set_metadata_value(metadata, 'title', preview_data.get('internationalTitle', {}).get('title'))
            self.set_metadata_value(metadata, 'original_title', preview_data.get('originalTitle', {}).get('title'))
            self.set_metadata_value(metadata, 'year', preview_data.get('year'))
            self.set_metadata_value(metadata, 'tagline', preview_data.get('plotOrDescriptionSynopsis'))
            if 'poster' in preview_data and 'path' in preview_data['poster']:
                poster = "https://fwcdn.pl/fpo" + preview_data['poster']['path']
                if poster not in metadata.posters:
                    metadata.posters[poster] = Proxy.Preview(HTTP.Request(poster).content)
            if 'genres' in preview_data and not metadata.genres:
                for genre in preview_data['genres']:
                    metadata.genres.add(genre.get('name', {}).get('text', ''))
                    Log("Added genre: %s" % genre['name']['text'])
            if 'directors' in preview_data and not metadata.directors:
                for director in preview_data['directors']:
                    metadata.directors.add(director.get('name', ''))
                    Log("Added director: %s" % director['name'])
            if 'mainCast' in preview_data and not metadata.roles:
                for cast_member in preview_data['mainCast']:
                    role = metadata.roles.new()
                    role.name = cast_member.get('name', '')
                    role.role = "Actor"
                    Log("Added cast member: %s as Actor" % cast_member['name'])
            if 'coverPhoto' in preview_data and 'photo' in preview_data['coverPhoto']:
                cover_photo = "https://fwcdn.pl/fph" + preview_data['coverPhoto']['photo'].get('sourcePath', '').replace('$', '7')
                if cover_photo not in metadata.art:
                    metadata.art[cover_photo] = Proxy.Preview(HTTP.Request(cover_photo).content)
            self.set_metadata_value(metadata, 'duration', preview_data.get('duration'))

