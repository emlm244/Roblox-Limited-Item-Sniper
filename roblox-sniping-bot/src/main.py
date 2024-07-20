from websocket_client import start_websocket
from auth import authenticate
from model_training import train_model
from config import Config
import time
from datetime import datetime, timedelta

def main():
    authenticate()
    next_model_update = datetime.now()
    model_update_interval = timedelta(days=Config.MODEL_UPDATE_INTERVAL)
    
    # Start the websocket client
    start_websocket()
    
    while True:
        # Check if it's time to update the model
        if datetime.now() >= next_model_update:
            for item_id in Config.TARGET_ITEM_IDS:
                train_model(item_id, force_retrain=True)
            next_model_update = datetime.now() + model_update_interval
        
        # Sleep for a day before checking again
        time.sleep(86400)  # 1 day in seconds

if __name__ == "__main__":
    main()
