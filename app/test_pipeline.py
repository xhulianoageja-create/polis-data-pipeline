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

def test_pipeline():
    print("1️⃣ Scraping...")
    quotes = scrape_quotes(URL)
    if quotes:
        print(f"  ✅ {len(quotes)} citate u scrape-uan")
    else:
        print("  ❌ Scraping dështoi!")

    print("2️⃣ API enrichment...")
    age_lookup = {}
    for q in quotes:
        author = q["author"]
        if author not in age_lookup:
            age_lookup[author] = enrich_with_age(author)
    print(f"  ✅ {len(age_lookup)} autorë u pasuruan me moshë")

    print("3️⃣ Transform...")
    processed_data = transform(quotes, age_lookup)
    print(f"  ✅ {len(processed_data)} records u transformuan")

    print("4️⃣ Encrypt...")
    encrypted_payload = encrypt_data(json.dumps(processed_data))
    print("  ✅ Të dhënat janë enkriptuar")

    print("5️⃣ Save...")
    save_encrypted({"payload": encrypted_payload}, DATA_PATH)
    print(f"  ✅ Data u ruajt te {DATA_PATH}")

    print("🎉 Pipeline testuar me sukses!")

if __name__ == "__main__":
    test_pipeline()
