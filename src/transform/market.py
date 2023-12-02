
from config import dataframe_timeframes

class Base:
    def __init__(self, symbol, name, dataframes=None):
        self.symbol = symbol
        self.name = name
        self.dataframes = dataframes if dataframes else {timeframe: None for timeframe in dataframe_timeframes}

    def __str__(self):
        return f'{self.__class__.__name__}(symbol={self.symbol}, name={self.name}, dataframes={self.dataframes})'

class Exchange(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.sectors = []

    def add_sector(self, sector):
        self.sectors.append(sector)

    def __str__(self):
        return super().__str__() + f', sectors={self.sectors}'

class Sector(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.industries = []

    def add_industry(self, industry):
        self.industries.append(industry)

    def __str__(self):
        return super().__str__() + f', industries={self.industries}'

class Industry(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.equities = []

    def add_equity(self, stock):
        self.equities.append(stock)

    def __str__(self):
        return super().__str__() + f', equities={self.equities}'

class Equity(Base):
    def __init__(self, symbol, name, dataframes):
        super().__init__(symbol, name)
        self.industry = None
        self.sector = None
        self.dataframes = dataframes
        
    # other methods...
