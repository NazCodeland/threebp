import datetime
import pandas as pd
import yfinance as yf
import time


# period : str
    # Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # Either Use period parameter or use start and end
# interval : str
    # Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # Intraday data cannot extend last 60 days

# intervals = timeframes
# intervals = {
#     '1m': '5d',  # For 1-minute timeframe, retrieve 5 days
# }

def download_ohlcv(symbols, intervals, market_hours=False):
    dfs = []
    for interval in intervals.keys():
        period = intervals[interval]
        start_time = time.time()
        try:
            if market_hours:
                start = intervals[interval]['start']
                end = intervals[interval]['end']
                df = yf.download(symbols, start=start, end=end, interval=interval, rounding=True, group_by='ticker', ignore_tz=True, keepna=True)

            else:
                df = yf.download(symbols, period=period, interval=interval, rounding=True, group_by='ticker', ignore_tz=True, keepna=True)
                # df = yf.download(symbols, start=intervals[interval]['start'], end=intervals[interval]['end'], interval=interval, rounding=True, group_by='ticker', ignore_tz=True, keepna=True)
                # df = df.tail(5)
                
            df = df.drop(columns='Adj Close', level=1)  # Remove 'Adj Close' column
            df.columns = df.columns.set_levels(df.columns.levels[1].str.lower(), level=1)  # Make column names lowercase
            df = df.assign(interval=interval)  # Add interval column
            df.set_index([pd.Index(df.index, name='date'), 'interval'], inplace=True)  # Set Interval as part of the index with column names
            dfs.append(df)

        except Exception as e:
            print(f"Failed to download data for symbols {symbols}, interval {interval}. Error: {e}")
            
        end_time = time.time()  # End the timer
        print(f"Time taken to download data for interval {interval}: {end_time - start_time} seconds")

    
    if not market_hours:
        df_all = pd.concat(dfs)
        return df_all
    else:
        return df

def categorize_interval_and_sort_data(df_all):

    # This line is converting the 'interval' column to a categorical data type with the specified categories and order.
    # The categories are '1m', '5m', '60m', '1d', '1wk', '1mo' and they are ordered. 
    # This means that they can be sorted or compared according to the order specified, which is useful for ordinal data.
    df_all['interval'] = pd.Categorical(df_all['interval'], categories=['1y', '1mo', '1wk', '1d', '60m', '5m', '1m'], ordered=True)

    # This will sort the DataFrame in the following way:
    # 1. 'symbol' in ascending order: This means the symbols will be sorted from A to Z.
    # 2. For each group of rows with the same symbol, 'interval' will be sorted in ascending order.
    # 3. For each group of rows with the same symbol and interval, 'date' will be sorted in descending order. 
    # This means the most recent dates will come first.
    df_all = df_all.sort_values(by=['symbol', 'interval', 'date'], ascending=[True, True, False])
    return df_all





# def single_download_ohlcv(symbol):
#     start_time = time.time()  # Start the timer
#         #     period : str
#         #     Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#         #     Either Use period parameter or use start and end
#         # interval : str
#         #     Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#         #     Intraday data cannot extend last 60 days
#     df = yf.download(symbol, period='1d')
#     print(df)
#     end_time = time.time()  # End the timer
#     print(f"Time taken to download data: {end_time - start_time} seconds")
#     return df


# https://query2.finance.yahoo.com/v8/finance/chart/MNS.TO?1509744000&1668748800&interval=1d&range=1mo&includePrePost=False

# TODO: look into these

# latest only showed 1 failed download:
# ['ACRG-B-U.CN']: Exception('%ticker%: No timezone found, symbol may be delisted')

# 11 Failed downloads:
# ['ACRG-B-U.CN', needs to be renamed to 'ACRG-BU.CN'
#  'CUR.V', ------ it is found
#  'UDOC.CN', ------ it is found
#  'FRNT.V',
#  'UDI.CN',
#  'NOVR.V',
#  'SHOE.CN',
#  'DST.CN',
#  'QREE.CN',
#  'RSM.V',
#  'UFC.V']: Exception('%ticker%: No price data found, symbol may be delisted (period=5d)')
