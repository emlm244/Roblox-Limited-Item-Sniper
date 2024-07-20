from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import joblib
import os
from datetime import datetime, timedelta
from data_preparation import fetch_historical_data, prepare_data
from config import Config
from logger import log_model_training
from alerts import send_model_training_alert

def train_model(item_id, force_retrain=False):
    model_path = f'data/model/random_forest_model_{item_id}.pkl'
    last_trained_path = f'data/model/last_trained_{item_id}.txt'
    
    try:
        # Log and send alert for starting model training
        log_model_training(item_id, 'start')
        send_model_training_alert(item_id, 'start')
        
        # Check if the model needs to be retrained
        if not force_retrain and os.path.exists(last_trained_path):
            with open(last_trained_path, 'r') as f:
                last_trained = datetime.strptime(f.read().strip(), '%Y-%m-%d')
                if datetime.now() - last_trained < timedelta(days=Config.MODEL_UPDATE_INTERVAL):
                    return load_model(item_id)
        
        data = fetch_historical_data(item_id)
        X_train, X_test, y_train, y_test = prepare_data(data)

        # Define the parameter grid
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }

        # Create a base model
        rf = RandomForestRegressor(random_state=42)

        # Instantiate the grid search model
        grid_search = GridSearchCV(estimator=rf, param_grid=param_grid,
                                   cv=3, n_jobs=-1, verbose=2, scoring='neg_mean_squared_error')

        # Fit the grid search to the data
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_

        # Save the best model
        joblib.dump(best_model, model_path)
        
        # Save the last trained date
        with open(last_trained_path, 'w') as f:
            f.write(datetime.now().strftime('%Y-%m-%d'))
        
        # Log and send alert for completing model training
        log_model_training(item_id, 'complete')
        send_model_training_alert(item_id, 'complete')
        
        return best_model
    
    except Exception as e:
        # Log and send alert for error in model training
        log_model_training(item_id, 'error')
        send_model_training_alert(item_id, 'error')
        raise e

def load_model(item_id):
    model_path = f'data/model/random_forest_model_{item_id}.pkl'
    return joblib.load(model_path)
