from tvDatafeed import TvDatafeed, Interval
import pandas as pd

def fetch_tv_data(symbol='EURUSD', exchange='FX_IDC', n=50):
    tv = TvDatafeed()
    try:
        df = tv.get_hist(symbol=symbol, exchange=exchange, interval=Interval.in_1_minute, n_bars=n)
        df = df.reset_index()
        df = df[['datetime', 'open', 'high', 'low', 'close', 'volume']]
        return df
    except Exception as e:
        print("❌ TVDatafeed Error:", e)
        return None
