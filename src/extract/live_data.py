import aiohttp
import asyncio
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Unix Timestamp date values, used for the range of historical data retrieval 
start_date = 1509744000  # corresponds to November 16, 2018
end_date = 1668748800  # corresponds to November 16, 2023

async def fetch(session, symbol, start_date, end_date, timeframe="1mo", interval="1d"):
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{symbol}?{start_date}&{end_date}&interval={interval}&range={timeframe}&includePrePost=False"
    async with session.get(url, headers=headers) as response:
        data = await response.json()
        return symbol, data['chart']['result'][0]['meta']['regularMarketPrice']

async def get_data_asynchronously(symbols, start_date, end_date):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for symbol in set(symbols):
            tasks.append(fetch(session, symbol, start_date, end_date))
        results = await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
    return results

industry_equities = [
			{ "symbol": "CVX.V", "name": "Cematrix Corp", "industry": "VBMT" },
			{ "symbol": "FBF.V", "name": "Fab-Form Industries Ltd", "industry": "VBMT" },
			{
				"symbol": "TBL.TO",
				"name": "Taiga Building Products Ltd",
				"industry": "VBMT"
			}
    ]
symbols = [equity['symbol'] for equity in industry_equities]
results = asyncio.run(get_data_asynchronously(symbols, start_date, end_date))
print('results length', len(results))
for symbol, market_time in results:
    print(f"{symbol}: {market_time}")

