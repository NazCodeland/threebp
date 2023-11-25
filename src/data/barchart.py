from typing import Optional
from playwright.async_api import Page, ElementHandle
from playwright.async_api import async_playwright
import asyncio

async def extract_symbol_and_name(page: Page, custom_element: Optional[ElementHandle]) -> list:
    return await page.evaluate("""(element) => {
        const shadowRoot = element ? element.shadowRoot : console.log("no element", element);
        if (!shadowRoot) {
            console.log("no shadowRoot", shadowRoot);
            return;
        }
        return Array.from(shadowRoot.querySelectorAll("set-class.row._grid_columns")).map((row) => {
            const symbol_cell = row.querySelector("div._cell.symbol text-binding");
            const symbol_name_cell = row.querySelector("div._cell.symbolName text-binding");
            const symbol_text = symbol_cell ? symbol_cell.shadowRoot.textContent : null;
            const company_name_text = symbol_name_cell ? symbol_name_cell.shadowRoot.textContent : null;
            return { symbol: symbol_text, symbolName: company_name_text };
        });
    }""", custom_element)

def filter_equities(rows: list) -> dict:
    non_equities = [row for row in rows if "-PR" in row['symbol'] or "-WT" in row['symbol'] or "-PF-" in row['symbol'] or "USD" in row['symbolName']]
    equities = [row for row in rows if not any(substring in row['symbol'] for substring in ["-PR", "-WT", "-PF-"]) and "USD" not in row['symbolName']]
    return {'equities': equities}

async def scroll_page_to_bottom(page: Page):
    return await page.evaluate("""() => {
        return new Promise((resolve) => {
            let totalHeight = 0;
            const distance = 100;
            const timer = setInterval(() => {
                const scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;
                if (totalHeight >= scrollHeight) {
                    clearInterval(timer);
                    resolve(true);
                }
            }, 100);
        });
    }""")

async def extract_industry_equities(industries):
    # If industries is a string, convert it to a list
    if isinstance(industries, str):
        industries = [industries]
        
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # object that gets returned
        industry_equities = {}

        for industry in industries:
            page = await context.new_page()
            url = f"https://www.barchart.com/stocks/quotes/-{industry}/components?orderBy=weightedAlpha&orderDir=desc&page=all"
            await page.goto(url)
            await scroll_page_to_bottom(page)
            await page.wait_for_selector("bc-data-grid")

            custom_element = await page.query_selector("bc-data-grid")
            rows = await extract_symbol_and_name(page, custom_element)

            if rows:
                equities = filter_equities(rows)
                industry_equities[industry] = equities

            # upload_to_db_barchart(industry_equities)  # You need to define this function in Python

            await page.close()

        await browser.close()

    return industry_equities

