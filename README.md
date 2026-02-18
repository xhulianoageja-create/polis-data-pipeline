# Data Pipeline Project – FINAL

## Përshkrimi i Projektit
Ky projekt implementon një **pipeline të plotë të përpunimit të të dhënave**:
1. Scraping – nxjerr citate dhe autorë nga faqja `http://quotes.toscrape.com`
2. API Enrichment – merr moshën e autorëve
3. Transform – pastron dhe organizon të dhënat
4. Encryption – enkripton të dhënat e përpunuara
5. Storage – ruan të dhënat e enkriptuara në `data/encrypted_data.json`

---
## Arkitektura dhe Rrjedha e të Dhënave

main.py -> scrape_quotes() -> enrich_with_age() -> transform() -> encrypt_data() -> save_encrypted()

---
### Python Version
Ky projekt kërkon **Python 3.9 ose më i lartë**.
Verifiko versionin me:
```powershell
python --version
Setup Hap Pas Hapi
1. Klono repo dhe futu në root
git clone <repo-url>
cd data-pipeline-final
2. Krijo dhe aktivizo virtual environment
python -m venv virtual26
.\virtual26\Scripts\activate
3. Instaloni libraritë
pip install --upgrade pip
pip install -r requirements.txt
4. Vendos .env
Në root të projektit:

SECRET_KEY=polis2026!
5. Run i Pipeline
Nga root i projektit:

python app\main.py
Pas ekzekutimit, folder-i data/ do të krijohet automatikisht dhe do të përmbajë encrypted_data.json.

6. Test i Pipeline
Për status hap pas hapi:

python app\test_pipeline.py
Ky skript tregon scraping, API enrichment, transform, encryption dhe storage.

Enkriptimi
Përdor Fernet symmetric encryption (cryptography).
Çelësi gjendet në .env si SECRET_KEY.
Të dhënat e ruajtura janë plotësisht të enkriptuara.

Libraritë kryesore
requests – për scraping dhe API

beautifulsoup4 – parsing HTML

cryptography – enkriptimi

python-dotenv – menaxhim i çelësave nga .env

Riprodhueshmëria
Fshi data/ dhe run përsëri main.py.

Pipeline krijon automatikisht folderin dhe file-in.