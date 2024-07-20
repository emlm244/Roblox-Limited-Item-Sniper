# Roblox Sniping Bot

A bot for sniping limited items on the Roblox marketplace. **Use at your own risk.**

## Disclaimer

This bot violates Roblox's Terms of Service (TOS). Using this bot can lead to account suspension or termination. By using this bot, you acknowledge that you are doing so at your own risk. The author is not responsible for any consequences resulting from the use of this bot. Additionally, you are responsible for managing the funds used by the bot. The bot's operation is provided "as is" without any guarantees of functionality or reliability.

## Features

### **Authentication**
- Securely authenticate with the Roblox API using environment variables.

### **Historical Data Analysis**
- **Fetch Historical Data**: Retrieve historical price data for target items.
- **Technical Indicators**:
  - Moving Averages
  - Exponential Moving Averages (EMA)
  - Relative Strength Index (RSI)

### **Real-Time Data Monitoring**
- Use WebSockets to receive real-time updates from the Roblox marketplace, minimizing delays.

### **Main Monitoring and Decision Loop**
- **Continuous Monitoring**: Continuously monitor the marketplace for new listings.
- **Trend Analysis

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/roblox-sniping-bot.git
    cd roblox-sniping-bot
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file based on the provided `.env.example`:
    ```sh
    cp .env.example .env
    ```

5. Fill in the `.env` file with your configuration details:
    - `ROBLOX_API_KEY`
    - `ALERT_EMAIL`

## Usage

1. Ensure you have the required historical data in the `data/historical_data` directory.

2. Run the bot:
    ```sh
    python src/main.py
    ```

## File Structure

- `data/`: Contains historical data, logs, and model files.
- `src/`: Contains the source code for the bot.
- `.env.example`: Example environment configuration file.
- `requirements.txt`: List of required Python packages.
- `README.md`: This file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
