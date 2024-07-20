import pandas as pd
from sklearn.model_selection import train_test_split

def fetch_historical_data(item_id):
    try:
        data = pd.read_csv(f'data/historical_data/{item_id}.csv')
        return data
    except FileNotFoundError:
        raise Exception(f"Historical data file for item {item_id} not found.")

def prepare_data(data):
    data['ema_10'] = data['price'].ewm(span=10, adjust=False).mean()
    data['rsi_14'] = calculate_rsi(data, 14)
    data = data.dropna()
    X = data[['ema_10', 'rsi_14']]
    y = data['price']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def calculate_rsi(data, period=14):
    delta = data['price'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()

    rs = avg_gain / avg_loss
    data[f'rsi_{period}'] = 100 - (100 / (1 + rs))
    return data
