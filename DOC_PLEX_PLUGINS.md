# Plex Plugins API Documentation 2024

I have gathered and described Plex Plugins API for you. It was a huge effort. If you like what I do, [support me](https://buymeacoffee.com/dejniel)

## Metadata Documentation
### Metadata for Agent.Movies Class

The following list describes the metadata available for movies in Plex using the `Agent.Movies` class:

#### Basic Metadata

- **title**: `String`
  - Movie title.

- **original_title**: `String`
  - Original movie title.

- **title_sort**: `String`
  - Movie title used for alphabetical sorting.

- **summary**: `String`
  - Movie description.

- **tagline**: `String`
  - Short description.

- **trivia**: `String`
  - Trivia related to the movie.

- **quotes**: `String`
  - Notable quotes from the movie.

- **year**: `Integer`
  - Year of movie production.

- **originally_available_at**: `Date`
  - Movie release date.

- **duration**: `Integer`
  - Duration of the movie in minutes.

#### Ratings

- **rating**: `Float`
  - Overall rating of the movie.

- **audience_rating**: `Float`
  - Rating given by the audience.

- **rating_image**: `String`
  - Image representing the movie rating. Only defined values like `imdb://image.rating`, `rottentomatoes://image.rating.ripe`, `rottentomatoes://image.rating.upright`, `themoviedb://image.rating`. To display both ratings, both icons must be set to `rottentomatoes`!

- **audience_rating_image**: `String`
  - Image representing the audience rating.

- **rating_count**: `Integer`
  - Number of ratings for the movie.

#### Detailed Information

- **content_rating**: `String`
  - Movie content rating.

- **content_rating_age**: `Integer`
  - Minimum recommended age for viewers.

- **studio**: `String`
  - Studio responsible for movie production.

#### Creators and Cast

- **directors**: `Set<Record>`
  - Set of movie directors, each `Record` object may contain additional information such as first name, last name, photo.

- **writers**: `Set<Record>`
  - Set of movie writers.

- **producers**: `Set<Record>`
  - Set of movie producers.

- **roles**: `Set<Record>`
  - Set of acting roles in the movie, each `Record` contains information about the actor and the role they play.

#### Artwork and Media

- **art**: `Dict<ProxyContainer>`
  - Background images and other graphical elements related to the movie.

- **posters**: `Dict<ProxyContainer>`
  - Movie posters.

- **banners**: `Dict<ProxyContainer>`
  - Promotional banners for the movie. (Not sure if this field is exclusively for TV shows)

- **themes**: `Dict<ProxyContainer>`
  - Music and sound themes related to the movie.

#### Categories and Tags

- **genres**: `Set<String>`
  - Movie genres.

- **collections**: `Set<String>`
  - Collections to which the movie belongs.

- **tags**: `Set<String>`
  - Tags related to the movie.

- **countries**: `Set<String>`
  - Countries of movie production.

#### Additional Information

- **chapters**: `Set<String>`
  - Chapters or segments of the movie.

- **reviews**: `Set<String>`
  - Movie reviews.

- **similar**: `Set<String>`
  - Movies similar or related to the current movie.

- **extras**: `[MediaContainer](https://python-plexapi.readthedocs.io/en/master/modules/base.html#plexapi.base.MediaContainer)`
  - Additional materials such as interviews, trailers, clips.

### Metadata Usage Details

#### ProxyContainer Usage Example

Example of adding images to metadata using `ProxyContainer`:

```python
# Adding an image to the 'art' collection
art_url = 'http://example.com/path/to/art.jpg'
metadata.art[art_url] = Proxy.Preview(HTTP.Request(art_url).content, sort_order=1)
```

`sort_order` is an optional parameter that specifies the display order of items in collections like `art`, `posters`, `banners`. It allows setting the display priority of these elements in the user interface. A lower `sort_order` value means a higher priority (e.g., an item with `sort_order=0` will appear before an item with `sort_order=1`).

#### Record Definition

`Record` is a class in the Plex API that represents a complex data record. `Record` objects can contain various attributes that are dynamically managed. They are particularly useful for storing detailed data about people (such as directors, actors) in movie metadata.

For example, a record for a director may contain attributes like:
- **name**: Name of the director.
- **photo**: URL to the director's photo.
- **role**: Specific role or function in the movie production.

```python
role = metadata.roles.new()
role.name = "Bruce Willis"
role.role = "Actor"
```

