
from extract.main import extract
from extract.yahoo_finance import download_from_yahoo
from transform.main import transform
from load.main import load
from utilities import save_df
import asyncio
from utilities import dict_to_dataframe
from transform.transform_functions import filter_rows, sanitize_data
from config import sector_industry_symbol_mapping
from config import sectors, industries, industry_equities
import json
import pickle

async def main():

		# raw data
		sectors, industries, industry_equities = await extract()
		exchange = transform(sectors, industries, industry_equities, sector_industry_symbol_mapping)
		# print("0---------------.----------------0")
		# with open('src/prices/exchange.json', 'w') as json_file:
		# 		json.dump(repr(exchange), json_file)

		# # Later on, you can deserialize the object from the file
		# with open('src/prices/exchange.pkl', 'rb') as file:
		# 		loaded_exchange = pickle.load(file)

		for sector in exchange.sectors:
			for industry in sector.industries:
				for equity in industry.equities:
					if equity.symbol == "NTR.TO":
						response = download_from_yahoo(equity.symbol, "1d") 
						equity.df = sanitize_data(response.text)

		for sector in exchange.sectors:
			for industry in sector.industries:
				for equity in industry.equities:
					if equity.df is not None and not equity.df.empty:
							await load(equity)
		

if __name__ == "__main__":
    asyncio.run(main())