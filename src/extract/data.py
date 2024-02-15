from typing import List, Dict
import pandas as pd
from extract.yfin import download_ohlcv
from extract.barchart import _load_cookies, _login, _save_cookies, _start_context, _stop_context, extract_sectors, extract_industries, extract_industry_equities
from load.database import download_from_db, upload_to_db

class Data:

    # barchart data
    @staticmethod
    async def _start_context():
        await _start_context()
    
    # barchart data
    @staticmethod
    async def _stop_context():
        await _stop_context()

    @staticmethod
    async def _login():
        await _login()
    
    @staticmethod
    async def _save_cookies():
        await _save_cookies()
        
    @staticmethod
    async def _load_cookies():
        await _load_cookies()

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
    def download_ohlcv(symbols: List[str], intervals: Dict[str, str], market_hours: bool = False) -> pd.DataFrame:
        return download_ohlcv(symbols, intervals, market_hours)

    # neon.tech postgressql database
    @staticmethod
    def download_from_db(tablename):
        return download_from_db(tablename)

    # neon.tech postgressql database
    @staticmethod
    def upload_to_db(df, symbol, timeframe):
        # This function would contain the code to upload data to a database
        return upload_to_db(df, symbol, timeframe)
