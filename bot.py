import time
from config import *
from delta_api import fetch_market_data, place_market_order
from strategy import generate_signal
from risk import calculate_sl_tp
from notifier import send_telegram
from datetime import datetime

print("[INFO] Starting live bot...")

while True:
    for symbol in SYMBOLS:
        market_data = fetch_market_data(symbol)
        if not market_data:
            continue
        try:
            signal, price = generate_signal(market_data)
            stop_loss, take_profit = calculate_sl_tp(price, signal, STOP_LOSS_PERCENT, TAKE_PROFIT_PERCENT)

            send_telegram(f"{signal} signal for {symbol} at {price}\nSL: {stop_loss:.2f}, TP: {take_profit:.2f}")
            print(f"[{datetime.now()}] Trade Signal for {symbol}: {signal} at {price}")
            place_market_order(symbol, signal, price)
        except Exception as e:
            print(f"[{datetime.now()}] Strategy error: {str(e)}")

    time.sleep(30)