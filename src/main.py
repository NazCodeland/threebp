
from extract.main import extract
from transform.main import transform
from load.main import load
from utilities import save_df
import asyncio
from utilities import dict_to_dataframe
from transform.transform_functions import filter_rows

async def main():
		# raw data
		sectors, industries, industry_equities = await extract()
		transformed_data = transform(sectors, industries, industry_equities)
		# load(transformed_data)

if __name__ == "__main__":
    asyncio.run(main())