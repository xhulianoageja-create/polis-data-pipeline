import json
import os

def save_encrypted(data, path):
    """
    Ruan të dhënat e enkriptuara në disk.
    Krijon automatikisht çdo folder mungues në rrugë.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
