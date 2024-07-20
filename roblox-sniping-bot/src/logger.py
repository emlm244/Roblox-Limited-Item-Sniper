import logging
from config import Config

logging.basicConfig(filename=Config.LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

def log_action(item_id, price, success):
    if success:
        logging.info(f"Successfully purchased item {item_id} at price {price}")
    else:
        logging.error(f"Failed to purchase item {item_id} at price {price}")

def log_model_training(item_id, status):
    if status == 'start':
        logging.info(f"Started training model for item {item_id}")
    elif status == 'complete':
        logging.info(f"Completed training model for item {item_id}")
    elif status == 'error':
        logging.error(f"Error during training model for item {item_id}")
