def calculate_sl_tp(entry_price, side, sl_pct, tp_pct):
    if side == 'BUY':
        stop_loss = entry_price * (1 - sl_pct / 100)
        take_profit = entry_price * (1 + tp_pct / 100)
    else:
        stop_loss = entry_price * (1 + sl_pct / 100)
        take_profit = entry_price * (1 - tp_pct / 100)
    return stop_loss, take_profit