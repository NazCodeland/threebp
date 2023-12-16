import pandas as pd
from transform.exchange import Exchange
from transform.transform_functions import filter_rows
from utilities import save_dataframe

def transform(sectors, industries, industry_equities):
    # Filter the sectors, industries, and equities data
    filtered_sectors = filter_rows(sectors)
    filtered_industries = filter_rows(industries)
    filtered_industry_equities = filter_rows(industry_equities)

    print("------------------------------------------------")
    print(filtered_sectors)
    print("------------------------------------------------")
    print(filtered_industries)
    print("------------------------------------------------")
    print(filtered_industry_equities)
    print("------------------------------------------------")
    
    save_dataframe(pd.DataFrame(filtered_sectors), 'sectors', 'json')
    save_dataframe(pd.DataFrame(filtered_industries), 'industries', 'json')
    save_dataframe(pd.DataFrame(filtered_industry_equities), 'industry_equities', 'json')
    
    exchange = Exchange('TSX', 'Toronto Stock Exchange', filtered_sectors, filtered_industries, filtered_industry_equities)

    # Return the fully built Exchange instance
    return exchange


