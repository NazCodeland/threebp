from transform.market import Exchange, Sector, Industry, Equity
from extract.yahoo_finance import download_from_yahoo
from config import dataframe_timeframes, sector_industry_symbols
import pandas as pd
from utilities import dict_to_dataframe
from transform.transform_functions import filter_rows

def create_sector(exchange, sector_symbol, sector_name):
    sector = Sector(sector_symbol, sector_name)
    exchange.add_sector(sector)
    return sector

def create_industry(sector, industry):
    industry_instance = Industry(industry['symbol'], industry['name'])
    sector.add_industry(industry_instance)
    return industry_instance

def create_equity(industry_instance, equity_data, dataframe_timeframes):
    dataframes = {}
    for timeframe in dataframe_timeframes:
        data = download_from_yahoo(equity_data['symbol'], timeframe)
        dataframes[timeframe] = data

    equity = Equity(equity_data['symbol'], equity_data['name'], dataframes)
    industry_instance.add_equity(equity)
    return equity

def transform(sectors, industries, industry_equities):
    sectors = filter_rows(sectors)
    industries = filter_rows(industries)
    industry_equities = filter_rows(industry_equities)    
    print(sectors)
    print(industries)
    print(industry_equities)

    # print(sectors)
    # print(industries)
    # print(industry_equities)
    # exchange = Exchange('TSX', 'Toronto Stock Exchange')
    # for sector_symbol, sector_name in sectors.items():
    #     sector = create_sector(exchange, sector_symbol, sector_name)


    #     sector.industries.append(sector_industry_symbols[sector_symbol])
    #     for industry_symbol, industry_name in sector_industry_symbols:
    #         industry_instance = create_industry(industry_symbol, industry_name)

    #         for equity_data in industry_equities.get(industry['symbol'], []):
    #             create_equity(industry_instance, equity_data, dataframe_timeframes)

    # return exchange




# TSX = Exchange("TSX")
# sectors = download_from_db("sectors")
# sector_industries = download_from_db("sector_industries")
# industry_equities = download_from_db("industry_equities")


# # add sectors
# for _, sector_row in sectors.iterrows():
#     sector_symbol = sector_row['symbol']
#     sector_symbol_name = sector_row['name']
#     # Create a Sector instance and add it to TSX
#     sector_instance = Sector(sector_symbol, sector_symbol_name)
#     TSX.add_sector(sector_instance)


# # add industries
# # Assuming sector_industries is a list of dictionaries
# df = pd.DataFrame(sector_industries)

# for _, row in df.iterrows():
#     industry_symbol = row['industrySymbol']
#     symbol = row['symbol']
#     symbol_name = row['name']

#     # Create an Industry instance
#     industry_instance = Industry(symbol, symbol_name)

#     # Find the sector this industry belongs to and add the industry to it
#     for sector in TSX.sectors:
#         if sector.symbol == industry_symbol:
#             sector.add_industry(industry_instance)
#             break


# # add equities
# # Assuming industry_equities is a list of dictionaries
# df_equities = pd.DataFrame(industry_equities)
# print(df_equities)
# for _, row in df_equities.iterrows():
#     equity_symbol = row['symbol']
#     equity_name = row['name']
#     industry_symbol = row['industry']

#     # Create an Equity instance
#     print("CALLING ONCE_------------")
#     equity_instance = Equity(equity_symbol, equity_name, download_from_yahoo(equity_symbol, "1d"))

#     # Find the industry this equity belongs to and add the equity to it
#     for sector in TSX.sectors:
#         for industry in sector.industries:
#             if industry.symbol == industry_symbol:
#                 industry.add_stock(equity_instance)
#                 break

# for sector in TSX.sectors:
#     print('sector::::::::::::::', sector)        
#     for industry in sector.industries:
#         print('industry::::::::::::::', industry)
#         for equity in industry.equities:
#             print('equity::::::::::::::', equity)        

# TSX.add_sector(Sector(""))
# TSX.process_industry_equities()
# TSX.process_sectors()
# TSX.process_industries()
# TSX.process_equities()

# for industry in industries:
#     TSX.add_sector(industry)

# print(TSX.sectors)
# print(TSX.industries)

