import asyncio
import aiohttp
from bs4 import BeautifulSoup
from pymongo import MongoClient
from multiprocessing import Pool, cpu_count
import logging

# Налаштування логів
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

# Підключення до MongoDB
client = MongoClient("mongodb+srv://valeriiakhylchenko:E4JSfcv8ytUWtBlH@cluster0.b6hq2v2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['buddhist']
coll = db['monasteries']

# Отримання HTML
async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except Exception as e:
        logging.error(f"Fetch error on {url}: {e}")
        return ""

# Парсинг сторінки
async def parse_page(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')

        try:
            name = soup.find('h1').text.strip() if soup.find('h1') else "Невідомо"
            location = soup.find('div', class_='location').text.strip() if soup.find('div', class_='location') else "Невідомо"
            description = soup.find('div', class_='description').text.strip() if soup.find('div', class_='description') else "Немає опису"
        except Exception as e:
            logging.warning(f"Parsing error on {url}: {e}")
            return

        # GPS-поля як заглушка
        gps = {"lat": 0.0, "lon": 0.0}

        monastery = {
            "name": name,
            "location": location,
            "gps": gps,
            "website": url,
            "description": description
        }

        try:
            coll.update_one({'name': name}, {'$set': monastery}, upsert=True)
            logging.info(f"Збережено: {name}")
        except Exception as e:
            logging.error(f"MongoDB error on {name}: {e}")

# Функція для multiprocessing
def worker(url):
    asyncio.run(parse_page(url))

# Головна функція
if __name__ == "__main__":
    urls = [
        "https://en.wikipedia.org/wiki/Wat_Phra_Dhammakaya",
        "https://en.wikipedia.org/wiki/Wat_Pho",
        "https://en.wikipedia.org/wiki/Kek_Lok_Si",
        "https://en.wikipedia.org/wiki/Tōdai-ji",
        "https://en.wikipedia.org/wiki/Wat_Arun",
        "https://en.wikipedia.org/wiki/Byodo-In_Temple",
        "https://en.wikipedia.org/wiki/Borobudur",
        "https://en.wikipedia.org/wiki/Shwedagon_Pagoda",
        "https://en.wikipedia.org/wiki/Boudhanath",
        "https://en.wikipedia.org/wiki/Mahabodhi_Temple"
    ]

    # Запускаємо з multiprocessing
    with Pool(processes=cpu_count()) as pool:
        pool.map(worker, urls)
