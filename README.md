# FilmWeb Standalone Agent for Plex

Many movies are rated differently in Poland compared to global standards. This plugin integrates Plex with the Polish Filmweb, providing ratings that reflect local preferences.

Są filmy, które oceniamy zupełnie inaczej w Polsce niż na świecie. Nie rozumiem, dlaczego nikt wcześniej (dobrze) nie zintegrował Plexa z polskim Filmwebem. Ale skoro tak, to ja to zrobiłem.

**O projekcie**
Oceny polskiego serwisu Filmweb są diametralnie różne od ocen globalnych. Są ku temu niezliczone powody, np. jakość dubbingu w francuskich filmach, jak *Asterix i Obelix*, które nie są szeroko znane poza Polską i Francją

**Wyzwania**
- Wtyczka – ogromnym wkładem mojej pracy – korzysta z tego samego [publicznego API (JSON)](DOC_FILMWEB_API.md), co strona Filmwebu i nie wymaga autoryzacji
- Ponieważ, jak wiadomo, [dokumentacja wtyczek Plexa](DOC_PLEX_PLUGINS.md) jest już zamknięta, także to wymagało wysiłku, aby zrozumieć poszczególne funkcje

**Potrzebujemy Ciebie!**
- To jest Open Source. Twoje [5zł miesięcznie](https://buymeacoffee.com/dejniel) zmienia wszytko i może uratować projekt! nawet pojedyncza wpłata może to zrobić. Utworzenie i utrzymanie takiego projektu to wiele dni z życia, twórcy naprawdę potrzebują tych symbolicznych wpłat, [pomóż mi dalej rozwijać projekt](https://buymeacoffee.com/dejniel)!
- Jeżeli jesteś programistą – nie ociągaj się z kontrybucją i zgłaszaniem błędów!


## Sposób działania i ograniczenia

### Wyszukiwanie i pobieranie danych z FilmWeb

Agent korzysta z dostępnego [API AJAX](DOC_FILMWEB_API.md), aby uprościć cały proces i pominąć zamknięte API FilmWeb oraz nie parsować strony. Niemniej może brakować szczegółowych metadanych.

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

### Brak logo FilmWeb

Plex ogranicza ustawianie innych, niż zdefinowane przez nich, ikonek ocen. Stąd nie mogę nigdzie umieścić loga FilmWebu.

### Zmiany API i przyszłość wtyczki

Weź pod uwagę, że według zapowiedzi twórców możliwość instalacji starych wtyczek miała być usunięta w wersji [Plex 1.41+](https://forums.plex.tv/t/important-information-for-users-running-plex-media-server-on-nvidia-shield-devices/883484) i [zastąpiona zupełnie nowym systemem wtyczek](https://forums.plex.tv/t/plex-fireside-in-the-forum-2024/885879/319). Tak się jednak nie stało. Stare wtyczki nadal działają, a dokumentacji nowych wtyczek nie widać. Nie wiadomo, czy nastąpi przerwa w działaniu wtyczek, niemniej zaktualizuję wtyczkę, jak tylko pojawi się dokumentacja nowego API wtyczek.

## Instalacja

Instrukcja ręcznej instalacji wtyczki jest opisana na [stronie Plexa](https://support.plex.tv/articles/201187656-how-do-i-manually-install-a-plugin/). Nie ma możliwości instalacji wtyczek w inny sposób ponieważ Plex [wycował się z nich](https://forums.plex.tv/t/discontinuation-of-plugins-watch-later-recommended-and-cloud-sync/312312) pod naciskiem korporacji Copyrightowych.

### W skrócie

1. **Pobierz kod źródłowy**: Skopiuj repozytorium lub pliki projektu do katalogu o nazwie kończącej się na ".bundle"
2. **Umieść w katalogu wtyczek Plex**: Umieść folder z wtyczką w folderze `Plex Media Server\Plug-ins`
3. **Uruchom ponownie Plex**: Po umieszczeniu wtyczki w odpowiednim folderze, uruchom ponownie serwer Plex Media Server.
4. **Konfiguracja**: Wejdź w ustawienia Plexa, wybierz zarządzanie agentami i ustaw `FilmWeb.pl` jako główne źródło metadanych dla filmów i seriali.

Przykładowe komendy dla Plexa w Dockerze z volumem configa w `plex_config`:
```bash
cd "/var/lib/docker/volumes/plex_config/_data/Library/Application Support/Plex Media Server/Plug-ins"
git clone "https://github.com/Dejniel/FilmWeb-Agent-for-Plex" "FilmWeb-Agent-for-Plex.bundle"
docker restart plex
```

### Użycie

Po skonfigurowaniu agenta, każdy nowy film lub serial będzie automatycznie wzbogacany o metadane z FilmWeb. Możesz także ręcznie wybrać opcję „Odśwież” dla poszczególnych pozycji w bibliotece, aby pobrać najnowsze informacje.

## Pomysły

Wszytkie pomysły i braki zebrane są w [TODO.md](TODO.md)

## Licencja

[Mozilla Public License Version 2.0](LICENSE.md)