import datetime
import pandas as pd
import yfinance as yf
import time



def download_ohlcv(symbols, intervals, market_hours=False):
    dfs = []
    for interval in intervals.keys():
        print('-------------------------------------')
        print("downloading data for:", interval)
        print('-------------------------------------')
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
    # df_all['interval'] = pd.Categorical(df_all['interval'], categories=['1y', '1mo', '1wk', '1d', '60m', '5m', '1m'], ordered=True)
    df_all['interval'] = pd.Categorical(df_all['interval'], categories=['1y', '1mo', '1wk', '1d', '60m'], ordered=True)

    # This will sort the DataFrame in the following way:
    # 1. 'symbol' in ascending order: This means the symbols will be sorted from A to Z.
    # 2. For each group of rows with the same symbol, 'interval' will be sorted in ascending order.
    # 3. For each group of rows with the same symbol and interval, 'date' will be sorted in descending order. 
    # This means the most recent dates will come first.
    df_all = df_all.sort_values(by=['symbol', 'interval', 'date'], ascending=[True, True, False])

    # re-order the columns from: ['date', 'interval', 'symbol', 'close', 'high', 'low', 'open', 'volume'] to:
    df_all = df_all.reindex(columns=['date', 'interval', 'symbol', 'open', 'high', 'low', 'close', 'volume'])

    return df_all


def download_financials():
    
        # Define the ticker symbol for the company you're interested in
        ticker_symbol = 'LIRC.TO'

        # Get the data for this ticker
        ticker_data = yf.Ticker(ticker_symbol)

        # Get the quarterly financials
        quarterly_financials = ticker_data.quarterly_financials

        # Reverse the order of the DataFrame
        quarterly_financials = quarterly_financials.iloc[::-1]

        # Select the rows for 'Total Revenue', 'Gross Profit' and 'Net Income'
        selected_financials = quarterly_financials.loc[['Total Revenue', 'Gross Profit', 'Net Income']]


        # Print the quarterly financials
        print(selected_financials)

# API LINK
# https://query2.finance.yahoo.com/v8/finance/chart/MNS.TO?1509744000&1668748800&interval=1d&range=1mo&includePrePost=False
