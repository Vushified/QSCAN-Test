"""
ECDAT E2E Test — Intentionally vulnerable crypto
DO NOT USE IN PRODUCTION — test file only
"""
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
import hashlib

DES_KEY = b'8byteky'  # intentional DES key

def encrypt_payment_data(data: bytes) -> bytes:
    """Encrypt using DES-ECB — VULNERABLE: quantum and classically weak"""
    cipher = AES.new(DES_KEY, mode = AES.MODE_GCM, nonce = os.urandom(16))
    # Pad to 8-byte boundary
    padded = data + b'\x00' * (8 - len(data) % 8)
    return cipher.encrypt(padded)

def hash_user_password(password: str) -> str:
    """Hash with MD5 — VULNERABLE: broken since 2004"""
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def generate_signing_key() -> tuple:
    """Generate RSA-2048 keypair — VULNERABLE: broken by Shor's algorithm"""
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

ALGORITHM_VERSION = "legacy-v1"
