"""Order service — imports from payment_service"""
from payment_service import process_payment

def create_order(items: list, card_number: str, pin: str) -> dict:
    total = sum(item["price"] for item in items)
    payment_result = process_payment(total, card_number, pin)
    return {
        "order_id": f"ORD-{hash(str(items)) % 100000:05d}",
        "items": items,
        "payment": payment_result
    }
