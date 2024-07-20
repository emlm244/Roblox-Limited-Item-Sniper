import pandas as pd
from data_preparation import calculate_rsi
from model_training import load_model

def predict_price(data):
    model = load_model()
    data['ema_10'] = data['price'].ewm(span=10, adjust=False).mean()
    data['rsi_14'] = calculate_rsi(data, 14)
    data = data.dropna()
    X = data[['ema_10', 'rsi_14']]
    predictions = model.predict(X)
    data['predicted_price'] = predictions
    return data