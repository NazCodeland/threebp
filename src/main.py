
from load.google_sheets import upload_to_gsheets
import asyncio
from transform.threebp import threebp
from transform.transform_functions import add_year_interval, get_file_as_df, merge_threebp_with_financials, save_to_html_and_open, tail_by_group, transform_financial_columns, wide_to_long, categorize_interval_and_sort_data
from extract.data import Data
import pandas_market_calendars as mcal

# --------------------------------------------------------------------
sectors = [
	{ "sector_symbol": "$TTGD", "sector_name": "TSX Financials Capped Index" },
	{ "sector_symbol": "TTFS", "sector_name": "TSX Financials Capped Index" },
	{ "sector_symbol": "TTMT", "sector_name": "TSX Materials Capped Index" },
	{ "sector_symbol": "TTEN", "sector_name": "TSX Energy Capped Index" },
	{ "sector_symbol": "TTIN", "sector_name": "TSX Industrials Capped Index" },
	{
		"sector_symbol": "TTTK",
		"sector_name": "TSX Information Tech Capped Index"
	},
	{ "sector_symbol": "TTUT", "sector_name": "TSX Utilities Capped Index" },
	{
		"sector_symbol": "TTCS",
		"sector_name": "TSX Consumer Staples Capped Index"
	},
	{ "sector_symbol": "TTRE", "sector_name": "TSX Real Estate Capped Index" },
	{
		"sector_symbol": "TTTS",
		"sector_name": "TSX Communication Services Capped Index"
	},
	{
		"sector_symbol": "TTCD",
		"sector_name": "TSX Consumer Discretionary Capped Index"
	},
	{ "sector_symbol": "TTHC", "sector_name": "TSX Health Care Capped Index" }
]

industries = [
	{ "industry_symbol": "VBVB", "industry_name": "TSX Beverages - Brewers" },
	{ "industry_symbol": "VSEM", "industry_name": "TSX Semiconductors" },
	{ "industry_symbol": "VSEQ", "industry_name": "TSX Semiconductor Equipment" },
	{
		"industry_symbol": "VPHR",
		"industry_name": "TSX Pharmaceutical Retailers"
	},
	{ "industry_symbol": "VENT", "industry_name": "TSX Entertainment" },
	{ "industry_symbol": "VMTF", "industry_name": "TSX Metal Fabrication" },
	{ "industry_symbol": "VCOC", "industry_name": "TSX Coking Coal" },
	{ "industry_symbol": "VTOB", "industry_name": "TSX Tobacco" },
	{ "industry_symbol": "VDCS", "industry_name": "TSX Discount Stores" },
	{ "industry_symbol": "VFIE", "industry_name": "TSX Financial Exchanges" },
	{ "industry_symbol": "VISS", "industry_name": "TSX Insurance - Specialty" },
	{ "industry_symbol": "VRCA", "industry_name": "TSX Resorts & Casinos" },
	{ "industry_symbol": "VFDD", "industry_name": "TSX Food Distribution" },
	{ "industry_symbol": "VSOL", "industry_name": "TSX Solar" },
	{ "industry_symbol": "VSCH", "industry_name": "TSX Specialty Chemicals" },
	{
		"industry_symbol": "VITS",
		"industry_name": "TSX Information Technology Srvs"
	},
	{ "industry_symbol": "VDRE", "industry_name": "TSX Diagnostics & Research" },
	{ "industry_symbol": "VBSD", "industry_name": "TSX Beverages - Soft Drinks" },
	{ "industry_symbol": "VBRO", "industry_name": "TSX Broadcasting" },
	{
		"industry_symbol": "VOGR",
		"industry_name": "TSX Oil & Gas Refining & Mrkt"
	},
	{ "industry_symbol": "VSHC", "industry_name": "TSX Shell Companies" },
	{ "industry_symbol": "VBMT", "industry_name": "TSX Building Materials" },
	{ "industry_symbol": "VLOD", "industry_name": "TSX Lodging" },
	{ "industry_symbol": "VBIO", "industry_name": "TSX Biotechnology" },
	{ "industry_symbol": "VINF", "industry_name": "TSX Insurance - Life" },
	{ "industry_symbol": "VPUB", "industry_name": "TSX Publishing" },
	{
		"industry_symbol": "VIPC",
		"industry_name": "TSX Insurance - Property & Casu"
	},
	{ "industry_symbol": "VMBS", "industry_name": "TSX Business Services" },
	{ "industry_symbol": "VPKF", "industry_name": "TSX Packaged Foods" },
	{ "industry_symbol": "VAPS", "industry_name": "TSX Apparel Stores" },
	{
		"industry_symbol": "VUIP",
		"industry_name": "TSX Utilities Independent Power"
	},
	{ "industry_symbol": "VRES", "industry_name": "TSX Real Estate Services" },
	{ "industry_symbol": "VPPP", "industry_name": "TSX Paper & Paper Products" },
	{ "industry_symbol": "VBOT", "industry_name": "TSX Bottom 100 Stocks" },
	{ "industry_symbol": "VOGM", "industry_name": "TSX Oil & Gas Midstream" },
	{ "industry_symbol": "VCEQ", "industry_name": "TSX Communication Equipment" },
	{ "industry_symbol": "VCSV", "industry_name": "TSX Credit Services" },
	{
		"industry_symbol": "VURE",
		"industry_name": "TSX Utilities Regulated Electric"
	},
	{ "industry_symbol": "VSRE", "industry_name": "TSX Specialty Retail" },
	{ "industry_symbol": "VHCP", "industry_name": "TSX Health Care Plans" },
	{
		"industry_symbol": "VRLS",
		"industry_name": "TSX Rental & Leasing Services"
	},
	{
		"industry_symbol": "VREV",
		"industry_name": "TSX Real Estate - Development"
	},
	{ "industry_symbol": "VBAG", "industry_name": "TSX Banks - Global" },
	{ "industry_symbol": "VSAP", "industry_name": "TSX Software - Application" },
	{ "industry_symbol": "VAGI", "industry_name": "TSX Agricultural Inputs" },
	{ "industry_symbol": "VIND", "industry_name": "TSX Insurance - Diversified" },
	{ "industry_symbol": "VUDI", "industry_name": "TSX Utilities Diversified" },
	{ "industry_symbol": "VOGI", "industry_name": "TSX Oil & Gas Integrated" },
	{
		"industry_symbol": "VDMM",
		"industry_name": "TSX Drug Manufacturers - Major"
	},
	{ "industry_symbol": "VAIR", "industry_name": "TSX Airlines" },
	{ "industry_symbol": "VOGE", "industry_name": "TSX Oil & Gas E&P" },
	{
		"industry_symbol": "VLWP",
		"industry_name": "TSX Lumber & Wood Production"
	},
	{ "industry_symbol": "VASM", "industry_name": "TSX Asset Management" },
	{ "industry_symbol": "VCOF", "industry_name": "TSX Confectioners" },
	{ "industry_symbol": "VTSE", "industry_name": "TSX Telecom Services" },
	{ "industry_symbol": "VAMN", "industry_name": "TSX Auto Manufacturers" },
	{ "industry_symbol": "VFOA", "industry_name": "TSX Footwear & Accessories" },
	{ "industry_symbol": "VSTL", "industry_name": "TSX Steel" },
	{ "industry_symbol": "VOGD", "industry_name": "TSX Oil & Gas Drilling" },
	{ "industry_symbol": "VCOG", "industry_name": "TSX Conglomerates" },
	{ "industry_symbol": "VGOL", "industry_name": "TSX Gold" },
	{ "industry_symbol": "VAAD", "industry_name": "TSX Aerospace & Defense" },
	{
		"industry_symbol": "VTCS",
		"industry_name": "TSX Indices Consumer Staples"
	},
	{ "industry_symbol": "VFMP", "industry_name": "TSX Farm Products" },
	{ "industry_symbol": "VGST", "industry_name": "TSX Grocery Stores" },
	{ "industry_symbol": "VTHC", "industry_name": "TSX Indices Health Care" },
	{
		"industry_symbol": "VPTC",
		"industry_name": "TSX Pollution Treatment Controls"
	},
	{ "industry_symbol": "VECO", "industry_name": "TSX Electronic Components" },
	{ "industry_symbol": "VSPO", "industry_name": "TSX Shipping & Ports" },
	{ "industry_symbol": "VPKC", "industry_name": "TSX Packaging & Containers" },
	{ "industry_symbol": "VBRE", "industry_name": "TSX Banks - Regional" },
	{
		"industry_symbol": "VEEP",
		"industry_name": "TSX Electrical Equipment & Parts"
	},
	{
		"industry_symbol": "VTTS",
		"industry_name": "TSX Indices Telecom Services"
	},
	{ "industry_symbol": "VMRF", "industry_name": "TSX Mortgage Finance" },
	{ "industry_symbol": "VCOE", "industry_name": "TSX Consumer Electronics" },
	{ "industry_symbol": "VAUP", "industry_name": "TSX Auto Parts" },
	{ "industry_symbol": "VRIS", "industry_name": "TSX REIT - Specialty" },
	{ "industry_symbol": "VMDD", "industry_name": "TSX Medical Devices" },
	{ "industry_symbol": "VTRU", "industry_name": "TSX Trucking" },
	{
		"industry_symbol": "VBWD",
		"industry_name": "TSX Beverages - Wine & Distiller"
	},
	{ "industry_symbol": "VLEI", "industry_name": "TSX Leisure" },
	{ "industry_symbol": "VTEN", "industry_name": "TSX Indices Energy" },
	{
		"industry_symbol": "VISL",
		"industry_name": "TSX Integrated Shipping & Logis"
	},
	{
		"industry_symbol": "VIMM",
		"industry_name": "TSX Industrial Metals Minerals"
	},
	{ "industry_symbol": "VITR", "industry_name": "TSX Internet Retail" },
	{
		"industry_symbol": "VHIS",
		"industry_name": "TSX Health Information Services"
	},
	{ "industry_symbol": "VCHE", "industry_name": "TSX Chemicals" },
	{ "industry_symbol": "VTIN", "industry_name": "TSX Indices Industrials" },
	{ "industry_symbol": "VGAM", "industry_name": "TSX Gambling" },
	{ "industry_symbol": "VAPM", "industry_name": "TSX Apparel Manufacturing" },
	{ "industry_symbol": "VAAA", "industry_name": "TSX Advertising Agencies" },
	{ "industry_symbol": "VTUT", "industry_name": "TSX Indices Utilities" },
	{
		"industry_symbol": "VEGC",
		"industry_name": "TSX Engineering & Construction"
	},
	{ "industry_symbol": "VSIL", "industry_name": "TSX Silver" },
	{
		"industry_symbol": "VHPP",
		"industry_name": "TSX Household & Personal Product"
	},
	{ "industry_symbol": "VTRS", "industry_name": "TSX Travel Services" },
	{
		"industry_symbol": "VFCE",
		"industry_name": "TSX Farm & Construction Equipt"
	},
	{
		"industry_symbol": "VDMS",
		"industry_name": "TSX Drug Specialty & Generic"
	},
	{
		"industry_symbol": "VSIM",
		"industry_name": "TSX Specialty Industrial Machine"
	},
	{ "industry_symbol": "VRRT", "industry_name": "TSX REIT - Retail" },
	{ "industry_symbol": "VRRE", "industry_name": "TSX REIT - Residential" },
	{ "industry_symbol": "VTFS", "industry_name": "TSX Indices Financials" },
	{ "industry_symbol": "VCSY", "industry_name": "TSX Computer Systems" },
	{ "industry_symbol": "VTRE", "industry_name": "TSX Indices Real Estate" },
	{
		"industry_symbol": "VSTI",
		"industry_name": "TSX Scientific & Technical Instr"
	},
	{ "industry_symbol": "VRDV", "industry_name": "TSX REIT - Diversified" },
	{
		"industry_symbol": "VRHF",
		"industry_name": "TSX REIT - Healthcare Faciltes"
	},
	{ "industry_symbol": "VAAS", "industry_name": "TSX Airports & Air Services" },
	{ "industry_symbol": "VTXS", "industry_name": "TSX Indices 60 Index" },
	{ "industry_symbol": "VPSS", "industry_name": "TSX Personal Services" },
	{ "industry_symbol": "VICI", "industry_name": "TSX Internet Content & Info" },
	{
		"industry_symbol": "VSIN",
		"industry_name": "TSX Software - Infrastructure"
	},
	{
		"industry_symbol": "VSPS",
		"industry_name": "TSX Security & Protection Srvs"
	},
	{ "industry_symbol": "VRST", "industry_name": "TSX Restaurants" },
	{ "industry_symbol": "VURG", "industry_name": "TSX Utilities Regulated Gas" },
	{
		"industry_symbol": "VTCD",
		"industry_name": "TSX Indices Consumer Discret"
	},
	{ "industry_symbol": "VLUG", "industry_name": "TSX Luxury Goods" },
	{
		"industry_symbol": "VTTK",
		"industry_name": "TSX Indices Information Tech"
	},
	{ "industry_symbol": "VHIM", "industry_name": "TSX Home Improvement Stores" },
	{ "industry_symbol": "VTMA", "industry_name": "TSX Textile Manufacturing" },
	{ "industry_symbol": "VRIN", "industry_name": "TSX REIT - Industrial" },
	{
		"industry_symbol": "VOPM",
		"industry_name": "TSX Other Precious Metals & Mine"
	},
	{ "industry_symbol": "VIDD", "industry_name": "TSX Industrial Distribution" },
	{ "industry_symbol": "VROF", "industry_name": "TSX REIT - Office" },
	{ "industry_symbol": "VCPM", "industry_name": "TSX Capital Markets" },
	{ "industry_symbol": "VTCO", "industry_name": "TSX Thermal Coal" },
	{ "industry_symbol": "VURA", "industry_name": "TSX Uranium" },
	{ "industry_symbol": "VRVE", "industry_name": "TSX Recreational Vehicles" },
	{ "industry_symbol": "VUTR", "industry_name": "TSX Utilities - Renewable" },
	{
		"industry_symbol": "VOGS",
		"industry_name": "TSX Oil & Gas Equipment & Srvs"
	},
	{ "industry_symbol": "VTMT", "industry_name": "TSX Indices Materials" },
	{ "industry_symbol": "VMDC", "industry_name": "TSX Medical Care" },
	{
		"industry_symbol": "VRED",
		"industry_name": "TSX Real Estate - Diversified"
	},
	{ "industry_symbol": "VWMA", "industry_name": "TSX Waste Management" },
	{ "industry_symbol": "VCOP", "industry_name": "TSX Copper" },
	{
		"industry_symbol": "VBPE",
		"industry_name": "TSX Building Products & Equpment"
	},
	{ "industry_symbol": "VTOP", "industry_name": "TSX Top 100 Stocks" },
	{
		"industry_symbol": "VMIS",
		"industry_name": "TSX Medical Instruments & Suppls"
	},
	{
		"industry_symbol": "VATD",
		"industry_name": "TSX Auto & Truck Dealerships"
	},
	{ "industry_symbol": "VINR", "industry_name": "TSX Insurance - Reinsurance" },
	{
		"industry_symbol": "VHFF",
		"industry_name": "TSX Home Furnishings & Fixture"
	},
	{
		"industry_symbol": "VEGM",
		"industry_name": "TSX Electronic Gaming & Media"
	}
]

industry_equities = [
        {
          "equity_symbol": "TECK-A.TO",
          "revLastQ": "N/A",
          "revGrowthLastQ": "unch",
          "revGrowth1qAgo": "unch",
          "revGrowth2qAgo": "unch",
          "grossProfitLastQ": "N/A",
          "operatingIncomeLastQ": "N/A",
          "netIncomeLastQ": "N/A",
          "revLastY": "N/A",
          "revGrowthLastY": "unch",
          "revGrowth1yAgo": "unch",
          "revGrowth2yAgo": "unch",
          "grossProfitLastY": "N/A",
          "operatingIncomeLastY": "N/A",
          "industry_symbol": "VIMM"
        },
        {
          "equity_symbol": "ACRG-B-U.CN",
          "revLastQ": "N/A",
          "revGrowthLastQ": "unch",
          "revGrowth1qAgo": "unch",
          "revGrowth2qAgo": "unch",
          "grossProfitLastQ": "N/A",
          "operatingIncomeLastQ": "N/A",
          "netIncomeLastQ": "N/A",
          "revLastY": "N/A",
          "revGrowthLastY": "unch",
          "revGrowth1yAgo": "unch",
          "revGrowth2yAgo": "unch",
          "grossProfitLastY": "N/A",
          "operatingIncomeLastY": "N/A",
          "industry_symbol": "VDMS"
        },	
        {
          "equity_symbol": "AAV.TO",
          "revLastQ": "143,027",
          "revGrowthLastQ": "+28.41%",
          "revGrowth1qAgo": "-24.65%",
          "revGrowth2qAgo": "-34.68%",
          "grossProfitLastQ": "95,275",
          "operatingIncomeLastQ": "43,274",
          "netIncomeLastQ": "28,314",
          "revLastY": "964,366",
          "revGrowthLastY": "+96.00%",
          "revGrowth1yAgo": "+100.76%",
          "revGrowth2yAgo": "-2.80%",
          "grossProfitLastY": "719,436",
          "operatingIncomeLastY": "537,267",
          "industry_symbol": "VCMP"
        },
        {
          "equity_symbol": "AIF.TO",
          "revLastQ": "185,232",
          "revGrowthLastQ": "-9.74%",
          "revGrowth1qAgo": "+7.54%",
          "revGrowth2qAgo": "+3.84%",
          "grossProfitLastQ": "N/A",
          "operatingIncomeLastQ": "10,790",
          "netIncomeLastQ": "929",
          "revLastY": "735,451",
          "revGrowthLastY": "+17.60%",
          "revGrowth1yAgo": "+11.45%",
          "revGrowth2yAgo": "-1.10%",
          "grossProfitLastY": "N/A",
          "operatingIncomeLastY": "52,052",
          "industry_symbol": "VTRE"
        }
      ]

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
		# equities = get_file_as_df('src/prices/industry_equities.json')
		# equities_list = equities['equity_symbol'].to_list()
		# equities_list = ["ERO.TO", "GWO.TO", "MFC.TO", "SHOP.TO", "TLRY.TO", "BIGG.CN", "PRL.TO"]
		# equities_list = ["BTC-USD", "ETH-USD"]
		equities_list = ["AEP.V", "BIGG.CN", "BITF.TO", "BITK.V", "CBIT.V", "CF.TO", "CNO."]


		print(':========STEP 1=========:')
		data = Data.download_ohlcv(equities_list, intervals_initial, market_hours=False)
		
		print(':========STEP 2=========:')
		data = wide_to_long(data)
		data = add_year_interval(data)
		data = tail_by_group(data)
		data = categorize_interval_and_sort_data(data)
		
		print(':========STEP 3=========:')            
		threebp_df = threebp(data)
		financials_df = get_file_as_df('src/prices/industry_equities.json')
		financials_df = transform_financial_columns(financials_df)
		threebp_and_financials = merge_threebp_with_financials(threebp_df, financials_df)
		save_to_html_and_open(threebp_and_financials)
		upload_to_gsheets(threebp_and_financials)
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
		# 				dataframes = Data.download_ohlcv(equities_list, intervals_daily, market_hours=True)
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
		# 				dataframes = Data.download_ohlcv(equities_list, intervals_daily, market_hours=True)
		# 				save_to_html_and_open(dataframes)

# ------------------------------------------------------------
		# market closed
		# dataframes = Data.download_ohlcv(equities_list, intervals_initial, market_hours=False)
		# save_to_html_and_open(dataframes)
		# sunday_data = process_data(dataframes)
		# threebp_main(sunday_data)


		# Save to a pickle file
		# sunday_data.to_pickle('data.pkl')

		# # # # Load 'sunday data' from a pickle file
		# sunday_data = pd.read_pickle('data.pkl')
# ------------------------------------------------------------

		# # 1 min data from Monday-Friday
		# weekday_data = Data.download_ohlcv(equities_list, intervals_daily)
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


		