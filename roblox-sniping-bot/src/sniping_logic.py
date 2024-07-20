import random
import time
from config import Config
from data_preparation import fetch_historical_data
from price_prediction import predict_price
from purchase import attempt_purchase
from logger import log_action
from alerts import send_alert

def handle_new_listing(data):
    item_id = data['item_id']
    current_price = data['price']
    historical_data = fetch_historical_data(item_id)
    predicted_data = predict_price(historical_data)

    predicted_price = predicted_data['predicted_price'].iloc[-1]

    # Example rule: Buy if current price is below predicted price
    if current_price < predicted_price * Config.PRICE_PREDICTION_RULES['price_threshold_percentage']:
        success = attempt_purchase(item_id, current_price)
        log_action(item_id, current_price, success)
        if success:
            send_alert(f"Successfully sniped item {item_id}", f"Price: {current_price}")

        # Implement random delay
        time.sleep(random.uniform(1, 3))