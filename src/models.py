import pandas as pd
import requests

class Exchange:
    def __init__(self, name):
        self.name = name
        self.sectors = []

    def add_sector(self, sector):
        self.sectors.append(sector)

    # methods related to sectors/weights...

class Sector:
    def __init__(self, name, timeframe, df):
        self.name = name
        self.timeframe = timeframe
        self.df = df
        
        self.industries = []

    def add_industry(self, industry):
        self.industry.append(industry)

    def add_stock(self, stock):
        self.stocks.append(stock)

    # methods to show what symbols belong to this sector...

class Industry(Sector):
    pass  # industry can inherit from sectors

class Stock:
    def __init__(self, symbol, sector, subsector):
        self.symbol = symbol
        self.sector = sector
        self.subsector = subsector
        # other properties...

    # methods specific to the stock...

# TSX = Exchange("TSX")

# for sector in sectors:
#     TSX.add_sector(sector)

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
