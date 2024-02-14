import asyncio
from extract.data import Data 

async def extract():
    await Data._start_context()
    sectors = await Data.download_sectors()
    industries = await Data.download_industries()
    await Data._login()
    industry_equities = await Data.download_industry_equities(industries)
    await Data._stop_context()

    return sectors, industries, industry_equities