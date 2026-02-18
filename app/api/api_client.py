import requests

API_URL = "https://api.agify.io"


def enrich_with_age(name):
    """
    Merr moshë të përafërt nga API.
    Nëse s'ka të dhëna → vendos default "Unknown".
    Trajton gabime të API-së dhe mungesë të të dhënave.
    """
    try:
        response = requests.get(API_URL, params={"name": name}, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Merr moshën ose vendos "Unknown" si default
        age = data.get("age") or "Unknown"

        # Log për informacion
        if age == "Unknown":
            print(f"Info: No age found for '{name}'")

        return age

    except requests.exceptions.RequestException as e:
        # Log për gabime dhe vendos default
        print(f"Warning: Could not fetch age for '{name}': {e}")
        return "Unknown"
