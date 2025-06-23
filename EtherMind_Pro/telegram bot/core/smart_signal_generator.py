import pandas as pd
import talib

def is_confirmed_signal(df):
    # 📊 EMA এবং RSI হিসাব করো
    df['ema10'] = talib.EMA(df['close'], timeperiod=10)
    df['ema20'] = talib.EMA(df['close'], timeperiod=20)
    df['rsi'] = talib.RSI(df['close'], timeperiod=14)

    # 🔍 সর্বশেষ ৭টি ক্যান্ডেল দেখো
    recent = df.tail(7)

    # ✅ BUY Signal: EMA10 > EMA20 for 7 candles & RSI below 70
    if all(recent['ema10'] > recent['ema20']) and df['rsi'].iloc[-1] < 70:
        return 'BUY'

    # ✅ SELL Signal: EMA10 < EMA20 for 7 candles & RSI above 30
    elif all(recent['ema10'] < recent['ema20']) and df['rsi'].iloc[-1] > 30:
        return 'SELL'

    # ❌ কোনো নিশ্চিত সিগন্যাল না থাকলে
    return None
