import smtplib
from email.mime.text import MIMEText
from config import Config
import logging

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = Config.ALERT_EMAIL
    msg['To'] = Config.ALERT_EMAIL

    try:
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            server.starttls()
            server.login(Config.ALERT_EMAIL, Config.EMAIL_PASSWORD)
            server.sendmail(Config.ALERT_EMAIL, [Config.ALERT_EMAIL], msg.as_string())
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")

def send_model_training_alert(item_id, status):
    subject = f"Model Training Update for Item {item_id}"
    if status == 'start':
        message = f"Started training model for item {item_id}."
    elif status == 'complete':
        message = f"Completed training model for item {item_id}."
    elif status == 'error':
        message = f"Error during training model for item {item_id}."
    send_alert(subject, message)
