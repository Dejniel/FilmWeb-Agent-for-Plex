# Filmweb API Documentation

I present to you a description of the publicly available Filmweb.pl API. The queries included here are used by the Filmweb website and do not require additional authorization

I have gathered and described the known endpoints for you. It was a huge effort. If you like what I do, [support me](https://buymeacoffee.com/dejniel)

## Overview

This API provides search functionality across various film and TV show entities in the Filmweb database. Users can perform searches using keywords, and the API returns information about films, TV shows, and actors that match the search criteria.

## API Endpoints

### Endpoint: Search for Movies and TV Shows

- **URL:** `https://www.filmweb.pl/api/v1/live/search`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (optional): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Query Parameters:**
  - `query` (required): The text query used to search for movies, TV shows, or people.
  - `pageSize` (optional): The number of search results to return per page. Default value is 10. Recommended value is 12, as used on the official site.

#### Description
This endpoint allows you to search for movies, TV shows, and people based on a given text query.

#### Response Description
- `total` (integer): The total number of results matching the query.
- `searchHits` (list of objects): The list of search results. Each result contains the following fields:
  - `id` (integer): The unique identifier of the result.
  - `type` (string): The type of the result (`film`, `serial`, `person`).
  - `matchedTitle` (string): The title of the found movie, TV show, or the name of the person.
  - `matchedLang` (optional, string): The language of the title or name.
  - `filmMainCast` (optional, list of objects): The list of actors in the movie or TV show.
    - `id` (integer): The unique identifier of the actor.
    - `name` (string): The name of the actor.

#### Note
Each result may contain varying levels of detail depending on the type (`film`, `serial`, `person`).


---

### Endpoint: Get Title Information

- **URL:** `https://www.filmweb.pl/api/v1/title/{id}/info`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the movie, TV show, or person for which information is being requested.

#### Description
This endpoint retrieves detailed information about a specific movie, TV show, or person by using its unique identifier.

#### Response Description
- `title` (string): The title of the movie or TV show.
- `originalTitle` (optional, string): The original title of the movie or TV show.
- `year` (integer): The release year of the movie or TV show.
- `otherYear` (optional, integer): An additional year related to the movie or TV show (e.g., end year for a TV series).
- `type` (string): The type of the entity (`film`, `serial`).
- `subType` (string): The subtype of the entity (`film_cinema`, `mini_serial`, `serial_tv`).
- `posterPath` (string): The relative path to the poster image of the movie or TV show.

---

### Endpoint: Get Film Description

- **URL:** `https://www.filmweb.pl/api/v1/film/{id}/description`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the movie for which the description is being requested.

#### Description
This endpoint retrieves a detailed description (synopsis) of a specific movie by using its unique identifier.

#### Response Description
- `id` (integer): The unique identifier of the movie.
- `synopsis` (string): The description or synopsis of the movie.
- `locale` (string): The locale for the provided description (e.g., `pl_PL`).
- `sourceType` (integer): The type of the source where the description is coming from.
- `main` (boolean): Indicates if this is the main description.
- `creationDate` (string): The creation date of the description.
- `entitySourceId` (optional, integer): Identifier of the source entity related to the description.

---

### Endpoint: Get Film Preview

- **URL:** `https://www.filmweb.pl/api/v1/film/{id}/preview`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the movie for which the preview information is being requested.

#### Description
This endpoint retrieves a preview of a specific movie, including details such as plot, genres, duration, cast, and directors.

#### Response Description
- `year` (integer): The release year of the movie.
- `entityName` (string): The type of entity (`film`, `serial`).
- `subType` (string): The subtype of the entity (`film_cinema`, `mini_serial`, `serial_tv`).
- `plot` (object): Contains the synopsis of the movie.
  - `synopsis` (string): The synopsis of the movie.
  - `sourceType` (integer): The type of the source for the synopsis.
  - `entitySourceId` (optional, integer): Identifier of the source entity related to the synopsis.
- `coverPhoto` (object): Contains information about the cover photo of the movie.
  - `id` (integer): The unique identifier of the cover photo.
  - `photo` (object): Details about the photo.
    - `id` (integer): The unique identifier of the photo.
    - `film` (integer): The ID of the film the photo is related to.
    - `sourcePath` (string): The path to the photo.
    - `fileExtension` (string): The file extension of the photo.
  - `mobilePath` (string): The path to the mobile version of the cover photo.
  - `verticalDisplacementInPercent` (integer): Vertical displacement of the cover photo in percent.
- `title` (object): Contains information about the movie title.
  - `title` (string): The title of the movie.
  - `country` (string): The country associated with the title.
  - `lang` (string): The language of the title.
- `originalTitle` (object): Contains information about the original title.
  - `title` (string): The original title of the movie.
  - `country` (string): The country associated with the original title.
  - `lang` (string): The language of the original title.
  - `original` (boolean): Indicates if this is the original title.
- `poster` (object): Contains information about the movie poster.
  - `lang` (string): The language of the poster.
  - `country` (string): The country associated with the poster.
  - `path` (string): The path to the poster image.
  - `fileExtension` (string): The file extension of the poster.
- `genres` (list of objects): List of genres associated with the movie.
  - `id` (integer): The unique identifier of the genre.
  - `name` (object): The name of the genre.
    - `text` (string): The genre name.
  - `nameKey` (string): The key for the genre name.
- `countries` (list of objects): List of countries involved in the movie's production.
  - `id` (integer): The unique identifier of the country.
  - `code` (string): The country code.
- `duration` (integer): The duration of the movie in minutes.
- `siteRecommends` (boolean): Indicates if the movie is recommended by the site.
- `mainReviewId` (integer): The unique identifier of the main review of the movie.
- `mainCast` (list of objects): List of main cast members in the movie.
  - `id` (integer): The unique identifier of the cast member.
  - `name` (string): The name of the cast member.
- `directors` (list of objects): List of directors of the movie.
  - `id` (integer): The unique identifier of the director.
  - `name` (string): The name of the director.
- `plotOrDescriptionSynopsis` (string): A short description or synopsis of the movie.  

---

### Endpoint: Get Top Roles for a Film

- **URL:** `https://www.filmweb.pl/api/v1/film/{id}/top-roles`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the movie for which the top roles are being requested.

#### Description
This endpoint retrieves the top roles for a specific movie, including details about the actors and their performance ratings.

#### Response Description
- The response is a list of objects, each representing a top role:
  - `id` (integer): The unique identifier of the role.
  - `count` (integer): The count of votes or mentions for this role.
  - `person` (integer): The unique identifier of the person (actor) playing the role.
  - `rate` (float): The rating of the actor's performance in the role.
  - `profession` (string): The profession of the person (e.g., `actors`).

---

### Endpoint: Get Film Counters

- **URL:** `https://www.filmweb.pl/api/v1/film/{id}/counters`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the movie for which the counters are being requested.

#### Description
This endpoint retrieves various counters for a specific movie, such as the number of awards, nominations, photos, posters, and more.

#### Response Description
- `awards` (integer): The number of awards won by the movie.
- `nominations` (integer): The number of nominations the movie has received.
- `photos` (integer): The number of photos available for the movie.
- `relateds` (integer): The number of related items (e.g., sequels, spin-offs).
- `episodes` (integer): The number of episodes if the movie is part of a series.
- `posters` (integer): The number of posters available for the movie.
- `videos` (integer): The number of videos available for the movie.
- `seasons` (optional, integer): The number of seasons if the movie is part of a series.
- `roleCounts` (object): Contains information about different roles associated with the movie.
  - `screenwriter` (integer): The number of screenwriters.
  - `director` (integer): The number of directors.
  - `cinematographer` (integer): The number of cinematographers.
  - `music` (integer): The number of music composers.
  - `productionDesigner` (integer): The number of production designers.
  - `actors` (integer): The number of actors.
  - `producer` (integer): The number of producers.
  - `montage` (integer): The number of people involved in editing (montage).
  - `costumeDesigner` (integer): The number of costume designers.
  - `sound` (integer): The number of people involved in sound production.
  - `originalMaterials` (optional, integer): The number of original material contributors.
  - `guest` (optional, integer): The number of guest appearances.
  - `voices` (optional, integer): The number of voice actors.

---

### Endpoint: Get Episodes for a Serial

- **URL:** `https://www.filmweb.pl/api/v1/serial/{id}/episodes`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the serial for which the episodes are being requested.
- **Query Parameters:**
  - `loadDates` (optional, boolean): Whether to load airing dates for each episode. Default value is `false`.

#### Description
This endpoint retrieves the list of episodes for a specific serial. It includes details such as episode number, duration, and airing dates for different countries.

#### Response Description
- The response is a list of objects, each representing an episode:
  - `id` (integer): The unique identifier of the episode.
  - `episodeNumber` (integer): The number of the episode in the season.
  - `duration` (optional, integer): The duration of the episode in minutes.
  - `airDates` (optional, list of objects): List of airing dates for the episode.
    - `airDateInt` (integer): The airing date in the format `YYYYMMDD`.
    - `country` (string): The country code for the airing date.

#### Note
- This endpoint only applies to serials. For other types, the response will be empty.
- The endpoint may return an error if the number of episodes exceeds a certain limit.


---

### Endpoint: Get Film Release Dates

- **URL:** `https://www.filmweb.pl/api/v1/film/{id}/dates`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the film for which the release dates are being requested.

#### Description
This endpoint retrieves various release dates for a specific film, including world release dates, public release dates, and the first airing date for serials.

#### Response Description
- `worldReleaseDate` (optional, object): Information about the initial world release date.
  - `dateInt` (integer): The release date in the format `YYYYMMDD`.
  - `country` (string): The country of the initial release.
  - `description` (optional, string): Description of the release (e.g., a film festival).
- `worldPublicReleaseDate` (optional, object): Information about the public world release date.
  - `dateInt` (integer): The public release date in the format `YYYYMMDD`.
  - `country` (string): The country of the public release.
  - `cinemasRelease` (boolean): Indicates if the release was in cinemas.
- `countryPublicReleaseDate` (optional, object): Information about the public release date in a specific country.
  - `dateInt` (integer): The public release date in the format `YYYYMMDD`.
  - `country` (string): The country of the public release.
  - `cinemasRelease` (boolean): Indicates if the release was in cinemas.
- `firstEpisodeDate` (optional, object): Information about the first episode airing date for serials.
  - `episodeId` (integer): The unique identifier of the first episode.
  - `airDateInt` (integer): The airing date in the format `YYYYMMDD`.
  - `country` (string): The country of the airing date.

#### Note
- This endpoint may return different types of dates depending on the type of entity (e.g., films vs. serials).
- Some fields may be optional depending on the availability of data.  


---

### Endpoint: Get Film Ratings

- **URL:** `https://www.filmweb.pl/api/v1/film/{id}/rating`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the film for which the ratings are being requested.

#### Description
This endpoint retrieves the ratings for a specific film, including the overall rating, the number of votes, and a breakdown of votes by rating.

#### Response Description
- `count` (integer): The total number of votes for the film.
- `rate` (float): The average rating of the film.
- `countWantToSee` (integer): The number of users who want to see the film.
- `countVote1` to `countVote10` (integer): The number of votes for each rating from 1 to 10.

---

### Endpoint: Get Critics' Ratings for a Film

- **URL:** `https://www.filmweb.pl/api/v1/film/{id}/critics/rating`
- **Method:** `GET`
- **Headers:**
  - `x-locale` (required): Specifies the language and regional settings. For example, `pl_PL` for Polish.
- **Path Parameters:**
  - `id` (required): The unique identifier of the film for which the critics' ratings are being requested.

#### Description
This endpoint retrieves the critics' ratings for a specific film, including the number of critics and the average rating given by them.

#### Response Description
- `count` (integer): The total number of critics who rated the film.
- `rate` (float): The average rating given by the critics.