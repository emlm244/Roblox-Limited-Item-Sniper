import requests
from config import Config

def authenticate():
    headers = {
        'Authorization': f'Bearer {Config.ROBLOX_API_KEY}'
    }
    try:
        response = requests.get('https://api.roblox.com/v1/auth', headers=headers)
        response.raise_for_status()
        return headers
    except requests.exceptions.RequestException as e:
        raise Exception('Authentication failed') from e
