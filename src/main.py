
import json
import time
from typing import List
import pandas as pd
from extract.main import extract
from extract.yfin import download_financials, download_financials_for_symbol
from load.google_sheets import upload_to_gsheets
import asyncio
from transform.main import transform
from transform.threebp import threebp
from transform.transform_functions import add_year_interval, merge_price_with_financials,tail_by_group, transform_financials, wide_to_long, categorize_interval_and_sort_data
from extract.data import Data
import pandas_market_calendars as mcal
import pandas_config

from utilities import get_file_as_df, save_dataframe, save_to_html_and_open

# --------------------------------------------------------------------

async def main():
		# sectors, industries, industry_equities = await extract()
		# exchange = transform(sectors, industries, industry_equities)
		
		# save_pickle_object(exchange, 'exchange')

		# exchange = load_pickle_object('exchange')

		# for sector in exchange.sectors:
		# 	for industry in sector.industries:
		# 		for equity in industry.equities:
		# 			print(equity.symbol)
		# 			equity.df = equity.download_ohlcv()

		# for sector in exchange.sectors:
		# 	for industry in sector.industries:
		# 		for equity in industry.equities:
		# 				await load(equity, exchange)
		

		# Define the intervals for the initial data download and processing
		# Calculate the start and end dates for each interval
		# now = datetime.datetime.now()
		# intervals_initial = {
		# 		'1m': {'start': now - timedelta(days=5), 'end': now},  # For 1-minute timeframe, retrieve 5 days
		# 		'5m': {'start': now - timedelta(days=5), 'end': now},  # For 5-minute timeframe, retrieve 5 days
		# 		'60m': {'start': now - timedelta(days=5), 'end': now},  # For 1-hour timeframe, retrieve 5 days
		# 		'1d': {'start': now - timedelta(days=5), 'end': now},  # For 1-day timeframe, retrieve 5 days
		# 		'1wk': {'start': now - timedelta(weeks=4), 'end': now - timedelta(weeks=1)},  # For 1-week timeframe, retrieve 1 month, omit current week
		# 		'1mo': {'start': now - timedelta(weeks=16), 'end': now - timedelta(weeks=4)}  # For 1-month timeframe, retrieve 3 months, omit current month
		# }
                
		# Define the intervals for the initial data download and processing
		# period : str
		# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
		intervals_initial = {
				# '1m': '5d',  # For 1-minute timeframe, retrieve 5 days
				# '5m': '5d',  # For 5-minute timeframe, retrieve 5 days
				'60m': '5d',  # For 1-hour timeframe, retrieve 5 days
				'1d': '5d',  # For 1-day timeframe, retrieve 5 days
				'1wk': '3mo',  # For 1-week timeframe, retrieve 1 month
				'1mo': '5y'  # For 1-month timeframe, retrieve 3 months
		}

		# TODO: perform check to see if any new industries are included inside of 
		# industries.json that are not within the 'sector_industry_name_mapping' inside of config.py
		#--------------------------------------------------------------------------------------------------
		# equities symbol
		# symbols = get_file_as_df('src\prices\industry_equities.json')
		# symbols = symbols['symbol'].to_list()
		# symbols = ["ERO.TO", "GWO.TO", "MFC.TO", "SHOP.TO", "TLRY.TO", "BIGG.CN", "PRL.TO"]
		# symbols = ["BTC-USD", "ETH-USD"]
		symbols = ["PRL.TO", "ERO.TO"]


		print('-------------: DOWNLOADING DATA')
		# price_data = Data.download_price(symbols, intervals_initial, market_hours=False)
		financial_data = download_financials(symbols, period="quarterly")
		# save_to_html_and_open(financial_data)
		# save_dataframe(price_data, "price_data", 'json')
		# save_dataframe(financial_data, "financials_data", 'json')


		# print('-------------: TRANSFORMING DATA')
		# price_data = wide_to_long(price_data)
		# price_data = add_year_interval(price_data)
		# price_data = tail_by_group(price_data)
		# price_data = categorize_interval_and_sort_data(price_data)
		# price_data = threebp(price_data)
  
		financial_data = transform_financials(financial_data)
		# threebp_and_financials = merge_price_with_financials(price_data, financial_data)

		# print('-------------: LOADING DATA')
		# save_to_html_and_open(threebp_and_financials)
		# upload_to_gsheets(threebp_and_financials)
                
		# call_apps_script()


# ------------------------------------------------------------
		# works! 5min intra-day data
		# while True:
		# now = datetime.datetime.now()
		# seconds_until_next_5_minutes = 300 - (now.minute * 60 + now.second) % 300
		# print('seconds_until_next_5_minutes', seconds_until_next_5_minutes)

		# start_time = now.replace(second=0, microsecond=0)
		# end_time = start_time + timedelta(minutes=5)
		# intervals_daily = {
		# 		'5m': {
		# 				'start': start_time,
		# 				'end': end_time
		# 		}
		# }
		# print('--------start', intervals_daily["5m"]['start'])
		# print('--------end', intervals_daily["5m"]['end'])
		# time.sleep(seconds_until_next_5_minutes)

		# if now.weekday() < 6 and ((now.hour == 9 and now.minute >= 31) or (10 <= now.hour < 16) or (now.hour == 16 and now.minute <= 1)):
		
# ------------------------------------------------------------
		# works! 5min intra-day data
		# while True:
		# 		now = datetime.timedelta.now()
		# 		seconds_until_next_5_minutes = 300 - (now.minute * 60 + now.second) % 300  # Change 300 to 302 here
		# 		# Pause execution until the start of the next 5-minute mark
		# 		print('seconds_until_next_5_minutes', seconds_until_next_5_minutes)
		# 		time.sleep(seconds_until_next_5_minutes)  

		# 		# Delay the function call by a few seconds to give the data source time to update
		

		# 		# Update 'now' after the sleep period
		# 		now = datetime.datetime.now()  
		# 		intervals_daily = {
		# 				'5m': {
		# 						'start': datetime.datetime(now.year, now.month, now.day, now.hour, now.minute-5),
		# 						'end': datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
		# 				}
		# 		}
		# 		print('--------start', intervals_daily["5m"]['start'])
		# 		print('--------end', intervals_daily["5m"]['end'])

		# 		# Mon-Fri 9:31AM - 4:01PM
		# 		if now.weekday() < 5 and ((now.hour == 9 and now.minute >= 31) or (10 <= now.hour < 16) or (now.hour == 16 and now.minute <= 1)):
		# 				dataframes = Data.download_ohlcv(symbols, intervals_daily, market_hours=True)
		# 				save_to_html_and_open(dataframes)



# ------------------------------------------------------------
		# works! 1min intra-day data
		# while True:
		# 		# Update 'now' and calculate the number of seconds until the next minute
		# 		now = datetime.datetime.now()
		# 		seconds_until_next_minute = 62 - now.second
		# 		time.sleep(seconds_until_next_minute)  # Pause execution until the start of the next minute

		# 		now = datetime.datetime.now()  # Update 'now' after the sleep period
		# 		intervals_daily = {
		# 				'1m': {
		# 						'start': datetime.datetime(now.year, now.month, now.day, now.hour, now.minute-1),
		# 						'end': datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
		# 				}
		# 		}

		# 		# Mon-Fri 9:31AM - 4:01PM
		# 		if now.weekday() < 5 and ((now.hour == 9 and now.minute >= 31) or (10 <= now.hour < 16) or (now.hour == 16 and now.minute <= 1)):
		# 				dataframes = Data.download_ohlcv(symbols, intervals_daily, market_hours=True)
		# 				save_to_html_and_open(dataframes)

# ------------------------------------------------------------
		# market closed
		# dataframes = Data.download_ohlcv(symbols, intervals_initial, market_hours=False)
		# save_to_html_and_open(dataframes)
		# sunday_data = process_data(dataframes)
		# threebp_main(sunday_data)


		# Save to a pickle file
		# sunday_data.to_pickle('data.pkl')

		# # # # Load 'sunday data' from a pickle file
		# sunday_data = pd.read_pickle('data.pkl')
# ------------------------------------------------------------

		# # 1 min data from Monday-Friday
		# weekday_data = Data.download_ohlcv(symbols, intervals_daily)
		# weekday_data = process_data(weekday_data)
		# # save_to_html_and_open(weekday_data)
		# # weekday_data = remove_first_row_each_symbol(weekday_data)

		# save_to_html_and_open(weekday_data)
		# # Use the 1-minute data to update all timeframes
		# df_all = update_timeframes(sunday_data, weekday_data)
		# save_to_html_and_open(df_all)

		# # Save the updated data back to the file
		# df_all.to_pickle('data.pkl')


		# # # threebp_main(df_all)
		# save_to_html_and_open(df_all)
		

		
if __name__ == "__main__":
    asyncio.run(main())


		