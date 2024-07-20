import websocket
import json
from config import Config
from sniping_logic import handle_new_listing  # Add this import

def on_message(ws, message):
    data = json.loads(message)
    if data['item_id'] in Config.TARGET_ITEM_IDS:
        handle_new_listing(data)

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws):
    print("WebSocket connection closed")

def on_open(ws):
    print("WebSocket connection opened")

def start_websocket():
    ws = websocket.WebSocketApp("wss://roblox-marketplace.com/realtime",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
