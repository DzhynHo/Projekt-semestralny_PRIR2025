# Projekt-semestralny_PRIR2025

# Buddhist Monasteries Scraper & Web App

## Opis projektu

Aplikacja do pobierania, przetwarzania oraz wizualizacji danych o buddyjskich klasztorach z różnych stron internetowych. Projekt pokazuje wykorzystanie wielowątkowości i asynchroniczności w Pythonie (multiprocessing, asyncio), parsowanie danych za pomocą BeautifulSoup, przechowywanie w MongoDB oraz prezentację danych przez interfejs webowy oparty na Flask. Całość działa w rozproszonym środowisku Docker z trzema kontenerami: scraper, backend Flask oraz MongoDB.

---

## Funkcjonalności

- Pobieranie danych o buddyjskich klasztorach (nazwa, lokalizacja, opis, zdjęcia, strona www)
- Asynchroniczne pobieranie danych z użyciem `aiohttp` i parsowanie HTML `BeautifulSoup`
- Wieloprocesowe przetwarzanie pobranych danych (multiprocessing)
- Zapis i aktualizacja danych w bazie MongoDB
- Graficzny interfejs webowy z mapą i listą klasztorów (Flask)
- Możliwość przejścia do szczegółowych danych konkretnego klasztoru
- Uruchomienie aplikacji w kontenerach Docker z wykorzystaniem docker-compose

---

## Technologie

- Python 3.8+
- aiohttp
- BeautifulSoup4
- multiprocessing
- Flask
- MongoDB
- Docker & Docker Compose

---

## Struktura projektu

- `/scraper` - kod scraper’a do pobierania i zapisywania danych
- `/gui` - backend Flask oraz szablony HTML dla interfejsu użytkownika
- `docker-compose.yml` - konfiguracja uruchomienia trzech kontenerów (MongoDB, scraper, Flask)

---

## Instrukcja uruchomienia

1. Sklonuj repozytorium:

```bash
git clone https://github.com/twoj-uzytkownik/buddhist-monasteries.git
cd buddhist-monasteries
