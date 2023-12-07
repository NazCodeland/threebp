from transform.exchange import Exchange
from transform.transform_functions import filter_rows

def transform(sectors, industries, industry_equities):
    # Filter the sectors, industries, and equities data
    filtered_sectors = filter_rows(sectors)
    filtered_industries = filter_rows(industries)
    filtered_equities = filter_rows(industry_equities)

    exchange = Exchange('TSX', 'Toronto Stock Exchange', filtered_sectors, filtered_industries, filtered_equities)

    # Return the fully built Exchange instance
    return exchange
