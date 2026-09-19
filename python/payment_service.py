"""Payment service — imports from crypto_utils"""
from crypto_utils import encrypt_payment_data, hash_user_password

def process_payment(amount: float, card_number: str, pin: str) -> dict:
    encrypted_card = encrypt_payment_data(card_number.encode())
    hashed_pin = hash_user_password(pin)
    return {
        "amount": amount,
        "encrypted_card": encrypted_card.hex(),
        "pin_hash": hashed_pin,
        "status": "processed"
    }

def refund_payment(transaction_id: str) -> dict:
    return {"transaction_id": transaction_id, "status": "refunded"}
