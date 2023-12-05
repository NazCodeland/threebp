
from config import dataframe_timeframes
import pandas as pd
from extract.yahoo_finance import download_from_yahoo

class Base:
    def __init__(self, symbol, name, df=None):
        self.symbol = symbol
        self.name = name
        self.df = pd.DataFrame(df) if df is not None else pd.DataFrame(columns=dataframe_timeframes)

    def __str__(self):
        return f'{self.__class__.__name__}(symbol={self.symbol}, name={self.name})'

    def download_data(self, timeframe):
        # List of possible attribute names for assets
        asset_attributes = ['sectors', 'industries', 'equities']

        # Check each attribute name to see if it exists and is a list
        for attr in asset_attributes:
            print(attr)
            if hasattr(self, attr) and isinstance(getattr(self, attr), list):
                # If the attribute exists and is a list, call download_data on each asset
                for asset in getattr(self, attr):
                    asset.download_data(timeframe)
                break  # Break after finding the first matching attribute
        else:
            # If none of the attributes exist, assume it's a single asset and download data
            self.df = download_from_yahoo(self.symbol, timeframe)

    def get_equity_by_symbol(self, symbol):
        # List of possible attribute names for assets
        asset_attributes = ['sectors', 'industries', 'equities']

        # Check each attribute name to see if it exists and is a list
        for attr in asset_attributes:
            if hasattr(self, attr) and isinstance(getattr(self, attr), list):
                # If the attribute exists and is a list, search for the equity with the given symbol
                for asset in getattr(self, attr):
                    if asset.symbol == symbol:
                        return asset
                    
class Exchange(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.sectors = []

    def __str__(self):
        return super().__str__() + f', sectors={self.sectors}'
    
    def __repr__(self):
        exchange_str = f"{self.__class__.__name__}(symbol={self.symbol}, name={self.name}, sectors=[\n"
        for sector in self.sectors:
            exchange_str += f"  {sector.__class__.__name__}(symbol={sector.symbol}, name={sector.name}, industries=[\n"
            for industry in sector.industries:
                exchange_str += f"    {industry.__class__.__name__}(symbol={industry.symbol}, name={industry.name}, equities=[\n"
                for equity in industry.equities:
                    exchange_str += f"      {equity.__class__.__name__}(symbol={equity.symbol}, name={equity.name})\n"
                exchange_str += "    ])\n"
            exchange_str += "  ])\n"
        exchange_str += "])"
        return exchange_str


    def add_sector(self, sector):
        self.sectors.append(sector)

class Sector(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.industries = []

    def __str__(self):
        return super().__str__() + f', industries={self.industries}'

    def add_industry(self, industry):
        self.industries.append(industry)


class Industry(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.equities = []

    def __str__(self):
        return super().__str__() + f', equities={self.equities}'

    def add_equity(self, stock):
        self.equities.append(stock)


class Equity(Base):
    def __init__(self, symbol, name, industry, sector, df=None):
        super().__init__(symbol, name, df)
        self.industry = industry
        self.sector = sector
        self.df = df
        
    # other methods...
