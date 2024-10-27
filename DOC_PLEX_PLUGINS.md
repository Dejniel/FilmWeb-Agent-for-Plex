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

## Constants in Plex Plugins

### HTTP Constant

`HTTP` is a constant within the Plex Plugin API that provides access to an instance of the `HTTPKit` class, designed for handling HTTP functions. Here's a detailed description of the properties and methods available through the `HTTP` constant.

#### Properties

- **CacheTime** (`int`): 
  - Specifies the cache duration for HTTP requests in seconds. It defaults to 0, which means caching is disabled.

#### Methods

- **ClearCache** (`instancemethod`):
  - Clears the HTTP cache for the current instance accessed via the `HTTP` constant.

- **ClearCookies** (`instancemethod`):
  - Removes all cookies stored in the current session accessed via the `HTTP` constant.

- **Cookies** (`instance`):
  - Returns a `MozillaCookieJar` object containing all cookies stored for the instance accessed via the `HTTP` constant.

- **CookiesForURL** (`instancemethod`):
  - Returns cookies associated with a specified URL accessed via the `HTTP` constant.

- **GetCookiesForURL** (`instancemethod`):
  - Retrieves cookies for a specified URL. This method appears to be a duplicate of `CookiesForURL` and may require further verification.

- **Headers** (`dict`):
  - Contains a dictionary of headers that will be used during HTTP requests accessed via the `HTTP` constant.

- **PreCache** (`instancemethod`):
  - Method for pre-caching data before it is actually requested via the `HTTP` constant.

- **RandomizeUserAgent** (`instancemethod`):
  - Changes the `User-Agent` header to a randomly generated one for each HTTP request made via the `HTTP` constant.

- **Request** (`instancemethod`):
  - Performs an HTTP request using defined headers, cookies, and other settings accessed via the `HTTP` constant.

- **SetCacheTime** (`instancemethod`):
  - Sets the cache duration for HTTP requests. It takes one `int` value representing time in seconds, accessible via the `HTTP` constant.

- **SetHeader** (`instancemethod`):
  - Allows setting or modifying HTTP headers for the current session accessed via the `HTTP` constant.

- **SetPassword** (`instancemethod`):
  - Sets a password if required for authentication within HTTP requests accessed via the `HTTP` constant.

- **SetTimeout** (`instancemethod`):
  - Sets a timeout limit for HTTP requests accessed via the `HTTP` constant.

### Client Constant (deprecated)

#### Overview
The `Client` object has been deprecated and removed from the Plex plugin APIs. This object provided fields such as:
- **Platform**: Type of client platform (e.g., iOS, Android, Windows).
- **Product**: Client's product name (e.g., Plex Media Player, Plex Web).
- **Protocols**: List of supported protocols.
- **Version**: Client version.

## Constants in Plex Plugins

### Platform Constant

`Platform` is a constant within the Plex Plugin API that provides access to an instance of the `PlatformKit` class with various attributes about the platform on which Plex is running. Here's a detailed description of the properties available through the `Platform` constant.

#### Properties

- **CPU** (`str`):
  - Represents the CPU architecture of the platform (e.g., `i386`).

- **HasFlash** (`bool`):
  - Indicates whether Adobe Flash is supported (e.g., `False`).

- **HasSilverlight** (`bool`):
  - Indicates whether Microsoft Silverlight is supported (e.g., `False`).

- **HasWebKit** (`bool`):
  - Indicates whether WebKit is supported (e.g., `False`).

- **MachineIdentifier** (`str`):
  - Provides the unique identifier of the Plex server (e.g., `0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f`).

- **OS** (`str`):
  - Specifies the operating system on which Plex is running (e.g., `Linux`).

- **OSVersion** (`str`):
  - Specifies the version of the operating system (e.g., `6.8.0-47-generic`).

- **ServerVersion** (`str`):
  - Indicates the version of the Plex server software (e.g., `1.41.0.8994-f2c27da23`).

### Plugin Constant

`PluginKit` is a constant within the Plex Plugin API that provides access to various methods and properties related to plugin management and operation. The instance of `PluginKit` is referred to as `Plugin` in the API. Here's a detailed description of the methods and properties available through the `Plugin` constant.

#### Properties

- **Identifier** (`str`):
  - The unique identifier for the plugin, such as `com.plexapp.agents.foo`.

- **Prefixes** (`list`):
  - A list of URL prefixes that the plugin handles. It typically includes routing paths.

- **ViewGroups** (`dict`):
  - A dictionary that stores view groups defined by the plugin, which help in organizing content presentation.

#### Methods

- **AddPrefixHandler** (`instancemethod`):
  - Binds a URL prefix to a function, allowing the plugin to handle requests at that URL.

- **AddViewGroup** (`instancemethod`):
  - Defines a new view group, which can be used to organize how data is presented in the Plex client.

- **Nice** (`instancemethod`):
  - Provides a mechanism to adjust the processing priority of the plugin, potentially improving performance under load.

- **Traceback** (`instancemethod`):
  - A method for generating a traceback from the current execution point, useful for debugging and error handling.

