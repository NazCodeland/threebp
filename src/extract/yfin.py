from typing import Any, Dict, List
import pandas as pd
import yfinance as yf
import time
import concurrent.futures

from utilities import save_dataframe

# API LINK
# https://query2.finance.yahoo.com/v8/finance/chart/MNS.TO?1509744000&1668748800&interval=1d&range=1mo&includePrePost=False

def download_ohlcv(symbols: list[str], intervals: dict[str, str], market_hours=False) -> pd.DataFrame:
    """
    Downloads OHLCV data for the given symbols and intervals.

    Parameters:
    symbols (list[str]): List of symbols to download data for.
    intervals (dict[str, str]): Dictionary mapping interval names to periods.
    market_hours (bool): Whether to only include market hours. Defaults to False.

    Returns:
    pd.DataFrame: A DataFrame with the following columns for each symbol:
        - 'open'
        - 'high'
        - 'low'
        - 'close'
        - 'volume'
    The DataFrame has a MultiIndex with the following levels:
        - 'date'
        - 'interval'
    """
    
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


def download_financials_for_symbol(symbol:str):
    symbol_data = yf.Ticker(symbol)
    quarterly_financials = symbol_data.financials

    quarterly_financials = quarterly_financials.iloc[::-1]    
    return quarterly_financials


def download_financials(symbols: List[str]) -> List[Dict['str', Dict['str', Any]]]:
    start_time = time.time()
    all_financials = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_symbol = {executor.submit(download_financials_for_symbol, symbol): symbol for symbol in symbols}
        for future in concurrent.futures.as_completed(future_to_symbol):
            symbol = future_to_symbol[future]
            try:
                # Get the financials data (yahoo finance provides the data in DataFrame format)
                financials = future.result()

                # Convert the DataFrame to a dictionary and convert the Timestamp objects to strings
                financials_dict = financials.to_dict()
                financials_dict = {str(k): v for k, v in financials_dict.items()}

                # Append the dictionary to the list with the symbol as a key
                all_financials.append({symbol: financials_dict})
            except Exception as exc:
                print(f'{symbol} generated an exception: {exc}')
    
    save_dataframe(all_financials, 'all_financials')
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")

    return all_financials








