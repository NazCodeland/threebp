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

    url = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start_date}&period2={end_date}&interval={timeframe}&events=history'
    print("url", url)
    response = requests.get(url, headers=headers)
    return response


