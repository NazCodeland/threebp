
from extract.main import extract
from transform.main import transform
from load.main import load
import asyncio
from utilities import load_pickle_object
# from config import sectors, industries, industry_equities

async def main():
		# sectors, industries, industry_equities = await extract()
		# exchange = transform(sectors, industries, industry_equities)
		
		# save_pickle_object(exchange, 'exchange')

		exchange = load_pickle_object('exchange')

		for sector in exchange.sectors:
			for industry in sector.industries:
				for equity in industry.equities:
					print(equity.symbol)
					equity.df = equity.download_ohlcv()

		# for sector in exchange.sectors:
		# 	for industry in sector.industries:
		# 		for equity in industry.equities:
		# 				await load(equity, exchange)
		

		# TODO: perform check to see if any new industries are included inside of 
		# industries.json that are not within the 'sector_industry_name_mapping' inside of config.py

if __name__ == "__main__":
    asyncio.run(main())



		