# FilmWeb Standalone Agent for Plex

> "Nigdy nie zrozumiem ocen na zagranicznych serwisach filmowych..."

Jeśli, jak ja, nie rozumiesz ocen na zagranicznych serwisach filmowych, ta wtyczka jest dla Ciebie! FilmWeb Standalone Agent umożliwia integrację ocen i metadanych z popularnego polskiego serwisu FilmWeb bez konieczności korzystania z zamkniętego API.&#x20;

Zapraszam do korzystania i współtworzenia wtyczki. W razie pytań, uwag lub problemów, proszę o kontakt przez GitHub.

Miłego oglądania! 🎬

#O Projekcie

## Funkcje

**Wyszukiwanie i pobieranie danych z FilmWeb**: Agent korzysta z dostępnego API AJAX, aby uprościć cały proces i pominąć zamknięte API FilmWeb oraz nie parsować strony. Niemniej może brakować szczegółowych metadanych.

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

## Instalacja

### Wymagania

- Plex Media Server z możliwością dodawania wtyczek.
- Python w wersji 3.8 lub wyższej.

### Krok po kroku

1. **Pobierz kod źródłowy**: Skopiuj repozytorium lub pliki projektu do katalogu wtyczek Plex.
2. **Umieść w katalogu wtyczek Plex**:
   - Dla systemu Linux: `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/`
   - Dla Windows: `%LOCALAPPDATA%\Plex Media Server\Plug-ins\`
3. **Uruchom ponownie Plex**: Po umieszczeniu wtyczki w odpowiednim folderze, uruchom ponownie serwer Plex Media Server.
4. **Konfiguracja**:
   - Wejdź w ustawienia Plexa, wybierz zarządzanie agentami i ustaw `FilmWeb.pl` jako główne źródło metadanych dla filmów i seriali.

## Użycie

Po skonfigurowaniu agenta, każdy nowy film lub serial będzie automatycznie wzbogacany o metadane z FilmWeb. Możesz także ręcznie wybrać opcję „Uaktualnij” dla poszczególnych pozycji w bibliotece, aby pobrać najnowsze informacje.

## Znane problemy i ograniczenia

- **Brak wsparcia dla zamkniętego API**: Wtyczka korzysta wyłącznie z dostępnego API AJAX, co oznacza, że niektóre funkcje dostępne w oficjalnym API mogą być pominięte.
- **Porównywanie tytułów**: Pomimo zastosowania `SequenceMatcher`, w niektórych przypadkach tytuły mogą nie zostać idealnie dopasowane, szczególnie jeśli różnice w tytułach są znaczące.


