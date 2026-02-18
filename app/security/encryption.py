import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import base64
import hashlib

load_dotenv()

def generate_key_from_password(password: str) -> bytes:
    """
    Gjeneron çelës Fernet nga tekst i thjeshtë.
    """
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

SECRET = os.getenv("SECRET_KEY")
fernet = Fernet(generate_key_from_password(SECRET))

def encrypt_data(data: str) -> str:
    """
    Enkripton string dhe kthen token.
    """
    return fernet.encrypt(data.encode()).decode()
