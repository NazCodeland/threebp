import yfinance as yf

interval_to_period = {
        '1m': '7d',  # 7 days of 1-minute data
        '5m': '60d',  # 60 days of 5-minute data
        '60m': '730d',  # 730 days of 1-hour data
        '1d': 'max',  # Maximum available data for 1-day interval
        '1mo': 'max'  # Maximum available data for 1-month interval
    }

def download_ohlcv(symbol):
    dataframes = {}
    for interval in interval_to_period.keys():
        period = interval_to_period[interval]
        try:
            print(f"----------------------START---{interval}----------------------")
            df = yf.download(symbol, period=period, interval=interval)
            dataframes[interval] = df
            print("-----------------------END---{}------------------")

        except Exception as e:
            print(f"Failed to download data for symbols {symbol}, interval {interval}. Error: {e}")
    return dataframes

