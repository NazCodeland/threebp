from extract.data import Data 

async def extract():
    await Data.start_context()
    sectors = await Data.download_sectors()
    industries = await Data.download_industries()
    industry_equities = await Data.download_industry_equities(industries)
    await Data.stop_context()

    return sectors, industries, industry_equities