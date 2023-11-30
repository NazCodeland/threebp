import pandas as pd
import requests
from database import download_from_db
from ast import literal_eval
from yahoo_finance import download_from_yahoo


    # symbol: str
    # timeframe: str = '1mo'
    # df: pd.DataFrame = None
    # _following: bool = False

    # @property
    # def following(self):
    #     return self._following

    # @following.setter
    # def following(self, value):
    #     self._following = value

    # @classmethod
    # def update_all(cls, instances):
    #     for instance in instances:
    #         instance.extract_industry_equities()

class Exchange:
    def __init__(self, name):
        self.name = name
        self.sectors = []
        

    def __str__(self):
        return f"Sector(name={self.name})"
    
    def add_sector(self, sector):
        self.sectors.append(sector)

    def process_sectors(self):
        sectors = download_from_db("sectors")
        for sector in sectors:
            pass
            # TSX.add_sector(Sector(sector, ))

    def process_industry_equities(self):
        industry_equities = download_from_db("industry_equities")        
        # Group by 'industry' and apply a lambda to convert each group into a dictionary
        result = industry_equities.groupby('industry').apply(lambda x: dict(zip(x.symbol, x.symbolName))).to_dict()
        return result

    # methods related to sectors/weights...

class Sector:
    def __init__(self, symbol, symbolName, timeframe="1d", df=None):
        self.symbol = symbol
        self.symbolName = symbolName
        self.timeframe = timeframe
        self.df = df
        
        self.industries = []

    def __str__(self):
        return f"Sector(name={self.symbol}, timeframe={self.timeframe})"
    

    def add_industry(self, industry):
        self.industries.append(industry)

    # methods to show what symbols belong to this sector...

class Industry():
    def __init__(self, symbol, name, timeframe="1d", df="None"):
        self.symbol = symbol
        self.name = name
        self.timeframe = timeframe
        self.df = df
        self.equities = []

    def add_stock(self, stock):
        self.equities.append(stock)

    def __str__(self):
        return f"Industry(symbol={self.symbol}, name={self.name}, timeframe={self.timeframe})"

class Equity:
    def __init__(self, symbol, industry, df=None):
        self.symbol = symbol
        self.industry = industry
        self.sector = sector
        self.df = df
        # other properties...

    def __str__(self):
        return f"Equity(symbol={self.symbol}, name={self.industry})"

    # methods specific to the stock...

TSX = Exchange("TSX")
sectors = download_from_db("sectors")
sector_industries = download_from_db("sector_industries")
industry_equities = download_from_db("industry_equities")


# add sectors
for _, sector_row in sectors.iterrows():
    sector_symbol = sector_row['symbol']
    sector_symbol_name = sector_row['symbolName']
    # Create a Sector instance and add it to TSX
    sector_instance = Sector(sector_symbol, sector_symbol_name)
    TSX.add_sector(sector_instance)


# add industries
# Assuming sector_industries is a list of dictionaries
df = pd.DataFrame(sector_industries)

for _, row in df.iterrows():
    industry_symbol = row['industrySymbol']
    symbol = row['symbol']
    symbol_name = row['symbolName']

    # Create an Industry instance
    industry_instance = Industry(symbol, symbol_name)

    # Find the sector this industry belongs to and add the industry to it
    for sector in TSX.sectors:
        if sector.symbol == industry_symbol:
            sector.add_industry(industry_instance)
            break


# add equities
# Assuming industry_equities is a list of dictionaries
df_equities = pd.DataFrame(industry_equities)
print(df_equities)
for _, row in df_equities.iterrows():
    equity_symbol = row['symbol']
    equity_name = row['symbolName']
    industry_symbol = row['industry']

    # Create an Equity instance
    print("CALLING ONCE_------------")
    equity_instance = Equity(equity_symbol, equity_name, download_from_yahoo(equity_symbol, "1d"))

    # Find the industry this equity belongs to and add the equity to it
    for sector in TSX.sectors:
        for industry in sector.industries:
            if industry.symbol == industry_symbol:
                industry.add_stock(equity_instance)
                break

for sector in TSX.sectors:
    print('sector::::::::::::::', sector)        
    for industry in sector.industries:
        print('industry::::::::::::::', industry)
        for equity in industry.equities:
            print('equity::::::::::::::', equity)        




# TSX.add_sector(Sector(""))
# TSX.process_industry_equities()
# TSX.process_sectors()
# TSX.process_industries()
# TSX.process_equities()


# for industry in industries:
#     TSX.add_sector(industry)

# print(TSX.sectors)
# print(TSX.industries)

# -------------------------------------------------------------------
# def create_symbol_name_dict_from_csv(file_path):
#     # Read the csv file
#     df = pd.read_csv(file_path)
#     df = df[["Symbol", "Name"]]

#     # Remove the leading ' -' from the symbols
#     df['Symbol'] = df['Symbol'].apply(lambda x: x.lstrip(' -'))

#     # Create a dictionary from the DataFrame
#     dict_df = df.set_index('Symbol')['Name'].to_dict()

#     return dict_df

# # Usage:
# file_path = "C:/Users/o0/Downloads/1-month-industry-performance-11-18-2023.csv"
# dict_df = create_symbol_name_dict_from_csv(file_path)
# print(dict_df)
# -------------------------------------------------------------------
