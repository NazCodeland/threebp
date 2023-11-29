from data import Data
from barchart import extract_industry_equities, extract_sectors
from database import download_from_db, upload_to_db
from config import sectors, industries, sector_industries, sector_and_industry_names
import pandas as pd
import asyncio
from utilities import save_df

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
# Upload sector_industries
# sector_industries = pd.DataFrame(list(sector_industries.items()), columns=['sector', 'industries'])
# print('df', sector_industries)
# upload_to_db(sector_industries, "sector_industries")

# Download sector_industries
# sector_industries_df = download_from_db("sector_industries")
# print(sector_industries_df)

# -----------------------------------------------------------------

# equities = download_from_db("equities")

# -----------------------------------------------------------------
# upload industry_equities
# industries = ['VURA', 'VOGI']
# industry_equities = asyncio.run(extract_industry_equities(industries))
# print(industry_equities)
# df_industry_equities = pd.DataFrame.from_dict(industry_equities)

# save_df(df_industry_equities, "industry_equities", "json")
# upload_to_db(df_industry_equities, "industry_equities")

# asyncio.run(extract_sectors())
industries = ['VURA', 'VOGI']
print(asyncio.run(extract_industry_equities(industries)))

# ------------------------------------------------------------------------------------------------------
# upload sector_industries to database
# Initialize an empty list to store the data
# data = []

# # Iterate over your dictionary
# for (sector_symbol, industries), industry_name_list in zip(sector_industries.items(), sector_and_industry_names.values()):
#     for i in range(len(industries)):
#         # Append each entry as a dictionary to the data list
#         data.append({'symbol': industries[i], 'symbolName': industry_name_list[i], 'industrySymbol': sector_symbol })

# # Convert the list of dictionaries to a DataFrame
# upload_to_db(df, "sector_industries")
# ------------------------------------------------------------------------------------------------------


