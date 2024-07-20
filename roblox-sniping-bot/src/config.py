import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ROBLOX_API_KEY = os.getenv('ROBLOX_API_KEY')
    TARGET_ITEM_IDS = [123456, 234567, 345678]
    MAX_PURCHASE_PRICE = 1000
    PRICE_PREDICTION_RULES = {
        'moving_average_period': 10,
        'price_threshold_percentage': 0.8,
    }
    ALERT_EMAIL = os.getenv('ALERT_EMAIL')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    LOG_FILE = 'data/logs/bot.log'
    MODEL_UPDATE_INTERVAL = 7  # days
