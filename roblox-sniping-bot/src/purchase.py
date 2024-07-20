import requests
from auth import authenticate

def attempt_purchase(item_id, price):
    headers = authenticate()
    payload = {
        'item_id': item_id,
        'price': price
    }
    try:
        response = requests.post('https://api.roblox.com/v1/purchase', headers=headers, json=payload)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        return False
