import re
from difflib import SequenceMatcher

def Start():
    Log("FilmWebStandaloneAgent is starting up.")

class Utils:
    @staticmethod
    def quote(s):
        """
        Encode a string for safe use in URLs.
        """
        safe = "/:"  # Define which characters are considered safe
        result = []
        for char in list(s):  # Convert string to list for iteration
            if char.isalnum() or char in safe:
                result.append(char)
            else:
                result.append('%{0:02X}'.format(ord(char)))
        return ''.join(result)
    @staticmethod
    def remove_bbcode(text):
        """
        Remove BBCode tags from a given text.
        """
        return re.sub(r'\[/?\w+.*?\]', '', text)

class FilmWebApi:
    BASE_URL = "https://www.filmweb.pl/api/v1"
    SEARCH_URL = BASE_URL + "/live/search?query=%s&pageSize=12"
    FILM_INFO_URL = BASE_URL + "/title/%s/info"
    DESCRIPTION_URL = BASE_URL + "/film/%s/description"
    RATING_URL = BASE_URL + "/film/%s/rating"
    CRITICS_RATING_URL = BASE_URL + "/film/%s/critics/rating"
    PREVIEW_URL = BASE_URL + "/film/%s/preview"

    @staticmethod
    def get_api(url):
        """
        Perform an API request and return the response.
        """
        headers = {'x-locale': 'pl_PL'}
        try:
            response = JSON.ObjectFromURL(url, headers=headers)
            if response:
                Log("API response received from %s" % url)
                return response
        except Exception as e:
            Log("API request error: %s" % e)
        return None

    @staticmethod
    def search(query):
        return FilmWebApi.get_api(FilmWebApi.SEARCH_URL % query)

    @staticmethod
    def get_film_info(film_id):
        return FilmWebApi.get_api(FilmWebApi.FILM_INFO_URL % film_id)

    @staticmethod
    def get_description(film_id):
        return FilmWebApi.get_api(FilmWebApi.DESCRIPTION_URL % film_id)

    @staticmethod
    def get_rating(film_id):
        return FilmWebApi.get_api(FilmWebApi.RATING_URL % film_id)

    @staticmethod
    def get_critics_rating(film_id):
        return FilmWebApi.get_api(FilmWebApi.CRITICS_RATING_URL % film_id)

    @staticmethod
    def get_preview(film_id):
        return FilmWebApi.get_api(FilmWebApi.PREVIEW_URL % film_id)

class FilmWebFilmAgent(Agent.Movies):
    name = 'FilmWeb.pl'
    languages = [Locale.Language.Polish]
    accepts_from = ['com.plexapp.agents.localmedia']

    def search(self, results, media, lang):
        FilmWebMedia.search(results, media, lang, "film")

    def update(self, metadata, media, lang):
        FilmWebMedia.update(metadata, media, lang)

# TODO: Implement FilmWebSerialAgent(Agent.TV_Shows) for handling TV shows

class FilmWebMedia:
    @staticmethod
    def search(results, media, lang, type):
        """
        Search for media on FilmWeb and append results to Plex.
        """
        
        excluded_words = [x.strip().lower() for x in Prefs['excludedKeys'].split(',')] + [str(media.year)]
        query = ' '.join(w for w in media.name.split() if w.lower() not in excluded_words)
        query_name = query
        query = "%s %s" % (query, media.year) if media.year else query
        query = Utils.quote(query)
        
        # Perform search API request
        Log("Performing search with query: %s" % query)
        search_response = FilmWebApi.search(query)
        search_results = search_response.get("searchHits", []) if search_response else []

        if not search_results:
            Log.Info("No search results found.")
            return 1

        order_num = 0

        for film_data in search_results:
            if film_data.get("type") != type:
                continue

            # Fetch additional information about the film
            Log("Fetching film info for ID: %s" % film_data['id'])
            film_info = FilmWebApi.get_film_info(film_data['id'])
            Log("Fetching film: %s" % film_info)
            if film_info:
                # Merge search data with additional info
                film_data.update(film_info)

                # Calculate similarity score
                score = FilmWebMedia.calculate_score(query_name, media, film_data, order_num)

                # Append result to Plex
                results.Append(MetadataSearchResult(
                    id=str(film_data['id']),
                    name=film_data['title'],
                    year=film_data['year'],
                    # TODO why doesnt work?
                    # thumb="https://fwcdn.pl/fpo" + film_data['posterPath'].replace('$', '1') if 'posterPath' in film_data else None,
                    score=score,
                    lang=lang
                ))
                Log("Added search result: %s with score %s" % (film_data['title'], score))

                order_num += 1

    @staticmethod
    def calculate_score(name, media, film_data, order_num):
        """
        Calculate similarity score between the provided media and search result.
        """
        year_penalty = 0
        if media.year:
            year_penalty = abs(int(media.year) - film_data['year'])
            if 'otherYear' in film_data:
                year_penalty = min(year_penalty, abs(int(media.year) - film_data['otherYear']))
            year_penalty = year_penalty * 4
        
        # Calculate title similarity using SequenceMatcher
        similarity_score = SequenceMatcher(None, name.lower(), film_data['title'].lower()).ratio()
        if 'originalTitle' in film_data:
            similarity_score = max(similarity_score, SequenceMatcher(None, name.lower(), film_data['originalTitle'].lower()).ratio())
        similarity_score = similarity_score * 100
        order_num = order_num - 1 if order_num <=0 else order_num
        return max(0, 10 + int(similarity_score) - year_penalty - (10 * order_num))

    @staticmethod
    def set_metadata_value(metadata, key, value):
        """
        Set metadata value if it is not already set.
        """
        if value and not getattr(metadata, key):
            setattr(metadata, key, value)
            Log("Set metadata %s to %s" % (key, value))

    @staticmethod
    def update(metadata, media, lang):
        """
        Update metadata for the given media.
        """
        
        # Fetch and set description
        description_data = FilmWebApi.get_description(metadata.id)
        if description_data:
            FilmWebMedia.set_metadata_value(metadata, 'summary', Utils.remove_bbcode(description_data.get('synopsis')))

        # Fetch and set audience rating
        rating_data = FilmWebApi.get_rating(metadata.id)
        if rating_data:
            FilmWebMedia.set_metadata_value(metadata, 'audience_rating', rating_data.get('rate'))
            # Only predefind icons works!
            # Only way to display both audience and critics rating is to set rottentomatoes icons (lol)!
            FilmWebMedia.set_metadata_value(metadata, 'audience_rating_image', 'rottentomatoes://image.rating.upright')

        # Fetch and set critics rating
        critics_rating_data = FilmWebApi.get_critics_rating(metadata.id)
        if critics_rating_data:
            FilmWebMedia.set_metadata_value(metadata, 'rating', critics_rating_data.get('rate'))
            FilmWebMedia.set_metadata_value(metadata, 'rating_count', critics_rating_data.get('count'))
            FilmWebMedia.set_metadata_value(metadata, 'rating_image', 'rottentomatoes://image.rating.ripe')

        # Fetch and set additional preview data
        preview_data = FilmWebApi.get_preview(metadata.id)
        if preview_data:
            FilmWebMedia.set_metadata_value(metadata, 'title', preview_data.get('internationalTitle', {}).get('title'))
            FilmWebMedia.set_metadata_value(metadata, 'original_title', preview_data.get('originalTitle', {}).get('title'))
            FilmWebMedia.set_metadata_value(metadata, 'year', preview_data.get('year'))
            FilmWebMedia.set_metadata_value(metadata, 'tagline', Utils.remove_bbcode(preview_data.get('plotOrDescriptionSynopsis')))

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
                cover_photo = "https://fwcdn.pl/fph" + preview_data['coverPhoto']['photo'].get('sourcePath', '').replace('$', '1')
                if cover_photo not in metadata.art:
                    metadata.art[cover_photo] = Proxy.Preview(HTTP.Request(cover_photo).content)

            FilmWebMedia.set_metadata_value(metadata, 'duration', preview_data.get('duration'))

