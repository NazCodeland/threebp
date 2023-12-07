
from extract.main import extract
from extract.yahoo_finance import download_from_yahoo
from transform.main import transform
from load.main import load
from utilities import save_df
import asyncio
from utilities import dict_to_dataframe
from transform.transform_functions import filter_rows, sanitize_data
from config import sectors, industries, industry_equities
import json
import pickle

async def main():

		# raw data
		sectors, industries, industry_equities = await extract()
		exchange = transform(sectors, industries, industry_equities)
		
		for sector in exchange.sectors:
			for industry in sector.industries:
				for equity in industry.equities:
					# response = download_from_yahoo(equity.symbol, "1d") 
					# equity.df = sanitize_data(response.text)
					equity.df = equity.download_ohlcv("1d")
					# await load(equity, exchange)
		
		for sector in exchange.sectors:
			for industry in sector.industries:
				for equity in industry.equities:
						await load(equity, exchange)
		

if __name__ == "__main__":
    asyncio.run(main())