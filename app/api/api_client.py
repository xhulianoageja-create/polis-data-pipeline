import requests

API_URL = "https://api.agify.io"

def enrich_with_age(name):
    """
    Merr moshë të përafërt nga API.
    Nëse s'ka të dhëna → kthen None.
    """
    try:
        response = requests.get(API_URL, params={"name": name}, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("age")
    except requests.exceptions.RequestException:
        return None
