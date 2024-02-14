import pandas as pd
from transform.exchange import Exchange
from transform.transform_functions import filter_data
from utilities import save_dataframe

def identify_new_entries(filtered_sectors, filtered_industries, filtered_industry_equities):
    # in the case of IPO's, new sectors (very unlikely but possible), industries, or just symbols missed, 
    # this function will catch them

    # Load the previous data
    try:
        old_sectors = pd.read_json('src/prices/sectors.json')
        old_industries = pd.read_json('src/prices/industries.json')
        old_industry_equities = pd.read_json('src/prices/industry_equities.json')

    except FileNotFoundError:
        print("Previous data not found.")
        return []

    # find new sectors, industries, equities not in the previous stored data
    new_sector_symbols = [item for item in filtered_sectors if item['symbol'] not in old_sectors['symbol'].tolist()]
    new_industry_symbols = [item for item in filtered_industries if item['symbol'] not in old_industries['symbol'].tolist()]
    new_equity_symbols = [item for item in filtered_industry_equities if item['symbol'] not in old_industry_equities['symbol'].tolist()]

    new_symbols = new_sector_symbols + new_industry_symbols + new_equity_symbols
    return new_symbols

def transform(sectors, industries, industry_equities):
    # Filter the sectors, industries, and equities data
    filtered_sectors = filter_data(sectors)
    filtered_industries = filter_data(industries)
    filtered_industry_equities = filter_data(industry_equities)

    save_dataframe(pd.DataFrame(filtered_sectors), 'new_sectors', 'json')
    save_dataframe(pd.DataFrame(filtered_industries), 'new_industries', 'json')
    save_dataframe(pd.DataFrame(filtered_industry_equities), 'new_industry_equities', 'json')
    
    new_entries = identify_new_entries(filtered_sectors, filtered_industries, filtered_industry_equities)
    if new_entries:
        save_dataframe(pd.DataFrame(new_entries), 'new_entries', 'json')

    # exchange = Exchange('TSX', 'Toronto Stock Exchange', filtered_sectors, filtered_industries, filtered_industry_equities)

    # Return the fully built Exchange instance
    # return exchange


