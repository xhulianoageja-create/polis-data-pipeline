import requests

API_URL = "https://api.agify.io"

def enrich_with_age(name):
    """
    Merr moshë të përafërt nga API.
    Nëse s'ka të dhëna → kthen None.
    Shton log nëse API dështon.
    """
    try:
        response = requests.get(API_URL, params={"name": name}, timeout=5)
        response.raise_for_status()
        data = response.json()
        age = data.get("age")
        if age is None:
            print(f"Info: No age found for '{name}'")
        return age
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not fetch age for '{name}': {e}")
        return None
