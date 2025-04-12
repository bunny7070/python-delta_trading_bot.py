import requests
import time
from datetime import datetime

API_KEY = 'yqa47IvNwHjzP6VDlCfuyWW5LUfKVV'
API_SECRET = 'fqTbbylycY6AsxjYis3oSVu141zarM4M6SfWKHhoSkVFX5WYtaEHsI28U8Dw'
BASE_URL = 'https://api.delta.exchange'

TRADING_SYMBOLS = ['BTCUSDT', 'ETHUSDT']
CAPITAL_PER_TRADE = 8  # USD per trade

def fetch_market_data(symbol):
    url = f"{BASE_URL}/v2/tickers"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"[{datetime.now()}] HTTP Error fetching data: {response.status_code} - {response.text}")
            return None

        data = response.json()
        tickers = data.get('result', [])
        for item in tickers:
            if item.get('symbol') == symbol:
                print(f"[{datetime.now()}] Raw market data for {symbol}: {item}")  # Debug print
                return item

        print(f"[{datetime.now()}] Symbol {symbol} not found in ticker data.")
        return None

    except Exception as e:
        print(f"[{datetime.now()}] Error fetching market data for {symbol}: {str(e)}")
        return None


def strategy_logic(market_data):
    try:
        last_price = float(market_data['mark_price'])  # Use correct price field
    except (KeyError, TypeError, ValueError):
        print(f"[{datetime.now()}] Strategy error: Missing price data.")
        return None, 0

    # Advanced sample logic (customize as needed)
    # Example: Buy if price is above 20 EMA (mock logic for now)
    signal = 'BUY' if int(last_price) % 2 == 0 else 'SELL'

    print(f"[{datetime.now()}] Trade Signal for {market_data['symbol']}: {signal} at {last_price}")
    return signal, last_price


def place_order(symbol, side, price):
    print(f"[{datetime.now()}] Placing {side} order for {symbol} at {price} with ${CAPITAL_PER_TRADE}")
    # Order placement via Delta API goes here
    pass

print("[INFO] Starting live bot with advanced strategy and diagnostics...")

while True:
    for symbol in TRADING_SYMBOLS:
        data = fetch_market_data(symbol)
        if not data:
            print(f"[{datetime.now()}] Skipped {symbol} due to invalid or missing data.")
            continue

        signal, price = strategy_logic(data)
        if signal != 'HOLD':
            place_order(symbol, signal, price)
        else:
            print(f"[{datetime.now()}] No trade signal for {symbol} (Price: {price})")

    time.sleep(30)
