from barchart import extract_industry_equities
from dataclasses import dataclass
import pandas as pd 
import asyncio
from yahoo_finance import download_from_yahoo

@dataclass
class Data:
    symbol: str
    timeframe: str = '1mo'
    df: pd.DataFrame = None
    _following: bool = 2

    @property
    def following(self):
        return self._following

    @following.setter
    def following(self, value):
        self._following = value

    @classmethod
    def update_all(cls, instances):
        for instance in instances:
            instance.extract_industry_equities()

    # barchart
    def download_industry_equity_list(self):
        # This function would contain the code to download data from Barchart
        # For this example, let's just return a dummy DataFrame
        self.df = asyncio.run(extract_industry_equities(self.symbol))

    def download_equity_OHLCV_data(self):
        if self.following:
            # This function would contain the code to download data from Yahoo
            # For this example, let's just return a dummy DataFrame
            self.df = download_from_yahoo(self.symbol, self.timeframe)

    def upload_to_db(self):
        # This function would contain the code to upload data to a database
        upload_to_db(self.df, self.symbol, self.timeframe)

    def download_from_db(self):
        # This function would contain the code to download data from a database
        self.df = download_from_db(self.symbol, self.timeframe)

        # Create an instance of the Data class
