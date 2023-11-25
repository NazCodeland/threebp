from data import Data
from barchart import extract_industry_equities
from database import download_from_db, upload_to_db
from config import sectors, industries, sector_and_industry_symbols
import pandas as pd
import asyncio
from utilities import save_df_as_csv

# -----------------------------------------------------------------
# Upload Sectors
# Convert the dictionary to a DataFrame
# sectors_df = pd.DataFrame(list(sectors.items()), columns=['symbol', 'symbolName'])
# upload_to_db(sectors_df, "sectors")

# Download Sectors
# sectors_df = download_from_db("sectors")
# print(sectors_df)

# -----------------------------------------------------------------
# Upload Industries
# industries_df = pd.DataFrame(list(industries.items()), columns=['symbol', 'symbolName'])
# upload_to_db(industries_df, "industries")

# Download industries
# industries_df = download_from_db("industries")
# print(industries_df)

# -----------------------------------------------------------------
# # Upload sector_industries
# sector_and_industry_symbols_df = pd.DataFrame(list(sector_and_industry_symbols.items()), columns=['sector', 'industries'])
# print('df', sector_and_industry_symbols_df)
# upload_to_db(sector_and_industry_symbols_df, "sector_industries")

# Download sector_industries
# sector_industries_df = download_from_db("sector_industries")
# print(sector_industries_df)

# -----------------------------------------------------------------

# equities = download_from_db("equities")

# -----------------------------------------------------------------
# upload industry_equities
# industries = ['VURA', 'VOGI']
# industry_equities = asyncio.run(extract_industry_equities(industries))

# rows = []
# for industry, info in industry_equities.items():
#     for equity in info['equities']:
#         row = equity.copy()  # create a copy of the equity dict
#         row['industry'] = industry  # add the industry to the dict
#         rows.append(row)

# industry_equities = pd.DataFrame(rows)
# upload_to_db(industry_equities, "industry_equities")
# -----------------------------------------------------------------

# download industry_equities
# industry_equities = download_from_db("industry_equities")
# save_df_as_csv(industry_equities, "industry_equities")
# print(industry_equities)
# -----------------------------------------------------------------
