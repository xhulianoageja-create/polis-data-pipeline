import json
import os

from scraping.scraper import scrape_quotes
from api.api_client import enrich_with_age
from processing.transformer import transform
from security.encryption import encrypt_data
from storage.database import save_encrypted

# URL për scraping
URL = "http://quotes.toscrape.com"

# Vendos rrugën absolute të root të projektit
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "encrypted_data.json")

def run_pipeline():
    # Step 1: scrape
    quotes = scrape_quotes(URL)

    # Step 2: enrich me API
    age_lookup = {}
    for q in quotes:
        author = q["author"]
        if author not in age_lookup:
            age_lookup[author] = enrich_with_age(author)

    # Step 3: transform
    processed_data = transform(quotes, age_lookup)

    # Step 4: encrypt
    encrypted_payload = encrypt_data(json.dumps(processed_data))

    # Step 5: save
    save_encrypted(
        {"payload": encrypted_payload},
        DATA_PATH
    )

if __name__ == "__main__":
    run_pipeline()
