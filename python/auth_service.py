"""Auth service — SHA-1 usage"""
import hashlib
import hmac

SECRET_KEY = b"supersecret"

def generate_session_token(user_id: str) -> str:
    """Generate session token using SHA-1 — VULNERABLE: SHAttered 2017"""
    return hashlib.sha1(f"{user_id}{SECRET_KEY}".encode()).hexdigest()

def verify_webhook(payload: bytes, signature: str) -> bool:
    """Verify webhook using HMAC-SHA1 — VULNERABLE"""
    expected = hmac.new(SECRET_KEY, payload, hashlib.sha1).hexdigest()
    return hmac.compare_digest(expected, signature)
