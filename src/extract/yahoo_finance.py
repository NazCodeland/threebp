import requests
import io
import pandas as pd
from config import start_date, end_date


def download_from_yahoo(symbol, timeframe):
    """
    Downloads stock data from Yahoo Finance.

    :param symbol: The ticker symbol of the stock.
    :type symbol: str
    :param timeframe: The timeframe for the stock data.
    :type timeframe: str

    This function takes a ticker symbol and a timeframe as parameters. It constructs a URL for the Yahoo Finance API, sends a GET request to this URL, and returns the response text.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    url = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start_date}&period2={end_date}&interval={timeframe}&events=history&includeAdjustedClose=true'
    print("url", url)
    response = requests.get(url, headers=headers)
    print(response.text)
    return sanitize_data(response.text)

def sanitize_data(data):
    # Read the string 'data' as a CSV file into a pandas DataFrame
    df = pd.read_csv(io.StringIO(data))
    # Reverse the order of the DataFrame rows
    # df = df.iloc[::-1]
    # delete the "Adj Close" column from the DataFrame
    sanitized_df = df.drop(columns=["Adj Close"])
    # Round all cells in the DataFrame to 2 decimal places
    sanitized_df = sanitized_df.round(2)
    # Reverse the DataFrame
    sanitized_df = sanitized_df.iloc[::-1]
    
    return sanitized_df

