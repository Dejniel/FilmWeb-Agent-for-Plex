# FilmWeb Standalone Agent for Plex

Many movies are rated differently in Poland than globally. This plugin integrates Plex with the Polish Filmweb, providing ratings that reflect local preferences

Są filmy, które oceniamy zupełnie inaczej w Polsce niż na świecie. Nie rozumiem, dlaczego nikt wcześniej (dobrze) nie zintegrował Plexa z polskim Filmwebem. Ale skoro tak, to ja to zrobiłem

**O projekcie**
Oceny polskiego serwisu Filmweb są diametralnie różne od ocen globalnych. Są ku temu niezliczone powody, np. jakość dubbingu w francuskich filmach, jak *Asterix i Obelix*, które nie są szeroko znane poza Polską i Francją

**Wyzwania**
- Wtyczka – ogromnym wkładem mojej pracy – korzysta z tego samego [publicznego API (JSON)](DOC_FILMWEB_API.md), co strona Filmwebu i nie wymaga autoryzacji
- Ponieważ, jak wiadomo, [dokumentacja wtyczek Plexa](DOC_PLEX_PLUGINS.md) jest już zamknięta, także to wymagało wysiłku, aby zrozumieć poszczególne funkcje

**Potrzebujemy Ciebie!**
- To jest Open Source. Twoje [5zł miesięcznie](https://buymeacoffee.com/dejniel) zmienia wszytko i może uratować projekt! nawet pojedyncza wpłata może to zrobić. Utworzenie i utrzymanie takiego projektu to wiele dni z rzycia, twórcy na prawdę potrzebuja tych symbolicznych wpłat, [pomóż mi dalej rozwijać projekt](https://buymeacoffee.com/dejniel)!
- Jeżeli jesteś programistą – nie ociągaj się z kontrybucją i zgłaszaniem błędów!


## Funkcje

**Wyszukiwanie i pobieranie danych z FilmWeb**: Agent korzysta z dostępnego [API AJAX](DOC_FILMWEB_API.md), aby uprościć cały proces i pominąć zamknięte API FilmWeb oraz nie parsować strony. Niemniej może brakować szczegółowych metadanych.

Pobierane są:

- Tytuł (polski i oryginalny)
- Opis fabuły
- Gatunki
- Obsada aktorska
- Reżyserzy
- Plakat i zdjęcie tła
- Ocena publiczności (ocena filmu na FilmWeb) oraz ocena (krytyków)

Metadane, których brakuje:

- Scenarzyści
- Producenci
- Dodatkowe multimedia (np. inne plakaty, zwiastuny)

Plex także ogranicza ustawinie innych, niż zdefinowane przez nich, ikonek. Stąd nie mogę nigdzie umieścić loga FilmWebu.

## Instalacja

Instrukcja ręcznej instalacji wtyczki jest opisana na [stronie Plexa](https://support.plex.tv/articles/201187656-how-do-i-manually-install-a-plugin/). Nie ma możliwości instalacji wtyczek w inny sposób ponieważ Plex [wycował się z nich](https://forums.plex.tv/t/discontinuation-of-plugins-watch-later-recommended-and-cloud-sync/312312) pod naciskiem korporacji Copyrightowych.

### W skrócie

1. **Pobierz kod źródłowy**: Skopiuj repozytorium lub pliki projektu do katalogu o nazwie kończącej się na ".bundle"
2. **Umieść w katalogu wtyczek Plex**: Umieść folder z wtyczką w folderze `Plex Media Server\Plug-ins`
3. **Uruchom ponownie Plex**: Po umieszczeniu wtyczki w odpowiednim folderze, uruchom ponownie serwer Plex Media Server.
4. **Konfiguracja**: Wejdź w ustawienia Plexa, wybierz zarządzanie agentami i ustaw `FilmWeb.pl` jako główne źródło metadanych dla filmów i seriali.

### Użycie

Po skonfigurowaniu agenta, każdy nowy film lub serial będzie automatycznie wzbogacany o metadane z FilmWeb. Możesz także ręcznie wybrać opcję „Odświerz” dla poszczególnych pozycji w bibliotece, aby pobrać najnowsze informacje.

## Pomysły

Wszytkie pomysły i braki zebrane są w [TODO.md](TODO.md)