import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_quotes(url):
    """
    Merr citate dhe autorë nga një faqe web.
    Kthen listë me dictionary.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = []

        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)

            quotes.append({
                "quote": text,
                "author": author
            })

        return quotes

    except requests.exceptions.RequestException as e:
        print(f"[SCRAPING ERROR] {e}")
        return []
