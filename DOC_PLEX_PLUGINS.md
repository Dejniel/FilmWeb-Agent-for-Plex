# Dokumentacja Metadanych dla Klasy Agent.Movies w Plex

Poniższa lista zawiera opis metadanych dostępnych dla filmów w Plex za pomocą klasy `Agent.Movies`:

## Podstawowe Metadane

- **title**: `String`
  - Tytuł filmu.

- **original_title**: `String`
  - Oryginalny tytuł filmu.

- **title_sort**: `String`
  - Tytuł filmu używany do sortowania alfabetycznego.

- **summary**: `String`
  - Opis filmu.

- **tagline**: `String`
  - Skrócony opis.

- **trivia**: `String`
  - Ciekawostki związane z filmem.

- **quotes**: `String`
  - Znaczące cytaty z filmu.

- **year**: `Integer`
  - Rok produkcji filmu.

- **originally_available_at**: `Date`
  - Data premiery filmu.

- **duration**: `Integer`
  - Czas trwania filmu w minutach.

## Oceny

- **rating**: `Float`
  - Ogólna ocena filmu.

- **audience_rating**: `Float`
  - Ocena przyznana przez widzów.

- **rating_image**: `String`
  - Grafika reprezentująca ocenę filmu. Tylko zdefiniowane wartości np. `imdb://image.rating`, `rottentomatoes://image.rating.ripe`, `rottentomatoes://image.rating.upright`, `themoviedb://image.rating`. Aby wyświetlały się obydwie oceny, obydwie ikonki muszą być ustawione na `rottentomatoes`!

- **audience_rating_image**: `String`
  - Grafika reprezentująca ocenę widzów.

- **rating_count**: `Integer`
  - Liczba ocen filmu.

## Szczegółowe Informacje

- **content_rating**: `String`
  - Klasyfikacja wiekowa filmu.

- **content_rating_age**: `Integer`
  - Minimalny zalecany wiek dla widzów.

- **studio**: `String`
  - Studio odpowiedzialne za produkcję filmu.

## Twórcy i Osoby

- **directors**: `Set<Record>`
  - Zestaw reżyserów filmu, każdy obiekt `Record` może zawierać dodatkowe informacje, takie jak imię, nazwisko, zdjęcie.

- **writers**: `Set<Record>`
  - Zestaw scenarzystów filmu.

- **producers**: `Set<Record>`
  - Zestaw producentów filmu.

- **roles**: `Set<Record>`
  - Zestaw ról aktorskich w filmie, każdy `Record` zawiera informacje o aktorze i roli, którą gra.

## Grafika i Media

- **art**: `Dict<ProxyContainer>`
  - Obrazy tła i inne elementy graficzne związane z filmem.

- **posters**: `Dict<ProxyContainer>`
  - Plakaty i afisze filmu.

- **banners**: `Dict<ProxyContainer>`
  - Banery promocyjne filmu.

- **themes**: `Dict<ProxyContainer>`
  - Motywy muzyczne i dźwiękowe związane z filmem.

## Kategorie i Tagi

- **genres**: `Set<String>`
  - Gatunki filmowe.

- **collections**: `Set<String>`
  - Kolekcje, do których film jest przypisany.

- **tags**: `Set<String>`
  - Tagi związane z filmem.

- **countries**: `Set<String>`
  - Kraje produkcji filmu.

## Dodatkowe Informacje

- **chapters**: `Set<String>`
  - Rozdziały lub segmenty filmu.

- **reviews**: `Set<String>`
  - Recenzje filmu.

- **similar**: `Set<String>`
  - Filmy podobne lub związane z bieżącym filmem.

- **extras**: `[MediaContainer](https://python-plexapi.readthedocs.io/en/master/modules/base.html#plexapi.base.MediaContainer)`
  - Dodatkowe materiały, takie jak wywiady, zwiastuny, klipy.

## Przykład Użycia ProxyContainer

Przykład dodawania obrazów do metadanych za pomocą `ProxyContainer`:

```python
# Dodawanie obrazu do kolekcji 'art'
art_url = 'http://example.com/path/to/art.jpg'
metadata.art[art_url] = Proxy.Preview(HTTP.Request(art_url).content, sort_order=1)
```

`sort_order` jest opcjonalnym parametrem, który określa kolejność wyświetlania elementów w kolekcjach takich jak `art`, `posters`, `banners`. Dzięki niemu można ustalić priorytet wyświetlania tych elementów w interfejsie użytkownika. Niższa wartość `sort_order` oznacza wyższy priorytet (np. element z `sort_order=0` pojawi się przed elementem z `sort_order=1`).

## Definicja Record

Record jest klasą w API Plex, która reprezentuje złożony rekord danych. Obiekty Record mogą zawierać różne atrybuty, które są dynamicznie zarządzane. Są one szczególnie użyteczne do przechowywania skomplikowanych danych o osobach (takich jak reżyserzy, aktorzy) w metadanych filmu. 

Przykładowo, rekord dla reżysera może zawierać takie atrybuty jak:
- name: Imię i nazwisko reżysera.
- photo: URL do zdjęcia reżysera.
- role: Specyficzna rola lub funkcja w produkcji filmu.

```python
role = metadata.roles.new()
role.name = "Bruce Willis"
role.role = "Actor"
```
