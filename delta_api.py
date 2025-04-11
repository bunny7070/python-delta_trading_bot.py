import requests
from config import API_KEY, API_SECRET, BASE_URL
from datetime import datetime

def fetch_market_data(symbol):
    try:
        response = requests.get(f"{BASE_URL}/v2/products")
        data = response.json()
        for item in data:
            if item.get('symbol') == symbol:
                print(f"[{datetime.now()}] Raw market data for {symbol}: {item}")
                return item
    except Exception as e:
        print(f"[{datetime.now()}] Error fetching market data for {symbol}: {str(e)}")
    return None

def place_market_order(symbol, side, price):
    print(f"[{datetime.now()}] Placing {side} order for {symbol} at {price} with ${CAPITAL_PER_TRADE}")
    # TODO: Add real order placement using authenticated API call