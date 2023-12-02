from extract.yahoo_finance import download_from_yahoo
from extract.barchart import start_context, stop_context, extract_sectors, extract_industries, extract_industry_equities
from load.database import download_from_db, upload_to_db

class Data:
    # barchart data
    @staticmethod
    async def start_context():
        await start_context()
    
    # barchart data
    @staticmethod
    async def stop_context():
        await stop_context()
    
    # barchart data
    @staticmethod
    async def download_sectors():
        # extracts sector and sector name for TSX
        return await extract_sectors()
    
    # barchart data
    @staticmethod
    async def download_industries():
        # extracts industry and industry name for TSX
        return await extract_industries()

    # barchart data
    @staticmethod
    async def download_industry_equities(industries):
        # extracts equities for a given industries list or a single industry
        return await extract_industry_equities(industries)

    # yahoo finance
    @staticmethod
    def download_from_yahoo(symbol, timeframe):
        return download_from_yahoo(symbol, timeframe)

    # neon.tech postgressql database
    @staticmethod
    def download_from_db(tablename):
        return download_from_db(tablename)

    # neon.tech postgressql database
    @staticmethod
    def upload_to_db(df, symbol, timeframe):
        # This function would contain the code to upload data to a database
        return upload_to_db(df, symbol, timeframe)
