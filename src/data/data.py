from yahoo_finance import download_from_yahoo
from barchart import setup_context, extract_sectors, extract_industries, extract_industry_equities
from database import download_from_db, upload_to_db

class Data:
    # barchart data
    @staticmethod
    async def setup_context():
        return await setup_context()
    
    # barchart data
    @staticmethod
    def extract_sectors(context):
        # extracts sector and sector name for TSX
        return extract_sectors(context)
    
    # barchart data
    @staticmethod
    def extract_industries(context):
        # extracts industry and industry name for TSX
        return extract_industries(context)

    # barchart data
    @staticmethod
    def extract_industry_equities(industries, context):
        # extracts equities for a given industries list or a single industry
        return extract_industry_equities(industries, context)

    # yahoo finance
    @staticmethod
    def download_equity_OHLCV_data(symbol, timeframe):
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