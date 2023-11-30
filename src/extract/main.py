from data import Data 
import asyncio

# extract/main.py
async def extract():
    p, context, browser = await Data.setup_context()
    sectors = await Data.download_sectors(context)
    industries = await Data.download_industries(context)
    equities = await Data.download_industry_equities(industries, context)

    await context.close()
    await browser.close()
    await p.stop()

    return { "sectors": sectors, "industries": industries, "equities": equities }


if __name__ == "__main__":
    asyncio.run(extract())