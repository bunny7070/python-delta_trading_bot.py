def generate_signal(price_data):
    mark_price = float(price_data.get("mark_price", 0))
    if mark_price == 0:
        raise ValueError("Missing mark_price")
    signal = "BUY" if int(mark_price) % 2 == 0 else "SELL"
    return signal, mark_price