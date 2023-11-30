from typing import Optional
from playwright.async_api import Page, ElementHandle
from playwright.async_api import async_playwright
from typing import List, Dict
from contextlib import asynccontextmanager


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

def filter_equities(rows: List[Dict]) -> List[Dict]:
    # This line creates a list of invalid symbols. It checks each row in the input list 'rows' and includes it in 'invalid_symbols' if the symbol contains "-PR", "-WT", "-PF-", or if the symbol name contains "USD".
    invalid_symbols = [row for row in rows if "-PR" in row['symbol'] or "-WT" in row['symbol'] or "-PF-" in row['symbol'] or "USD" in row['symbolName']]
    
    # This line creates a list of valid symbols. It checks each row in the input list 'rows' and includes it in 'valid_symbols' if the symbol does not contain "-PR", "-WT", "-PF-", "-B", "USD", or "Cl B".
    # It also modifies the symbol in each row based on certain conditions:
    # - If the symbol ends with '.VN', it replaces '.VN' with '.V'.
    # - If the symbol starts with '$', it removes the '$'.
    # - If the symbol starts with '-', it removes the '-'.
    valid_symbols = [dict(row, symbol=row['symbol'].replace('.VN', '.V')) if row['symbol'].endswith('.VN') else dict(row, symbol=row['symbol'].replace('$', '')) if row['symbol'].startswith('$') else dict(row, symbol=row['symbol'].lstrip('-')) if row['symbol'].startswith('-') else row for row in rows if not any(substring in row['symbol'] for substring in ["-PR", "-WT", "-PF-", "-B"]) and "USD" not in row['symbolName'] and "Cl B" not in row['symbolName']]
    
    # The function returns the list of valid symbols.
    return valid_symbols

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
async def scroll_page_to_top(page: Page):
    return await page.evaluate("""() => {
        return new Promise((resolve) => {
            const distance = 100;
            const timer = setInterval(() => {
                if (window.scrollY > 0) {
                    window.scrollBy(0, -distance);
                } else {
                    clearInterval(timer);
                    resolve(true);
                }
            }, 100);
        });
    }""")

# a helper function to create and return a context manager
@asynccontextmanager
async def setup_context():
    """
    This function creates and returns a context manager that can be used with the 'with' statement.
    The context manager creates a Playwright object, a browser instance, and a context object when the context is entered.
    The context manager closes the context, the browser, and the Playwright object when the context is exited.
    The function returns an async generator-iterator that yields the context and the browser objects.
    """
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context()

    try:
        yield context
    # close the context, the browser, and the Playwright object
    finally:
        await context.close()
        await browser.close()
        await p.stop()

async def extract_data(url, context, page: Optional[Page] = None):
    if page is None:
        page = await context.new_page()
        await page.goto(url)
    await scroll_page_to_bottom(page)
    await page.wait_for_selector("bc-data-grid")

    custom_element = await page.query_selector("bc-data-grid")
    rows = await extract_symbol_and_name(page, custom_element)

    await page.close()

    return rows

async def extract_sectors():
    # object that gets returned
    sectors = {}

    url = "https://www.barchart.com/search?q=$TT&regions=ca&assets=indices"
        
    # use a context manager to create and close the context and browser
    async with setup_context() as context:
        rows = await extract_data(url, context)

        if rows:
            filtered_rows = filter_equities(rows)
            for row in filtered_rows:
                symbol = row['symbol']
                symbol_name = row['symbolName']
                sectors[symbol] = symbol_name

    return sectors

async def extract_industries():
    # object that gets returned
    industries = {}

    url = "https://www.barchart.com/ca/stocks/sectors/industry-performance?orderBy=priceChange&orderDir=desc"

    # use a context manager to create and close the context, browser and playwright instance
    async with setup_context() as context:

        page = await context.new_page()
        await page.goto(url)

        # Uncheck the checkbox
        await page.evaluate("""() => {
            let checkbox = document.querySelector('#show-industrial');
            if (checkbox.checked) {
                checkbox.click();
            }
        }""")

        await scroll_page_to_bottom(page)
        await page.click('.show-all.ng-scope')
        await scroll_page_to_top(page)

        rows = await extract_data(url, context, page)

        if rows:
            filtered_rows = filter_equities(rows)
            for row in filtered_rows:
                symbol = row['symbol']
                symbol_name = row['symbolName']
                industries[symbol] = symbol_name

    return industries

async def extract_industry_equities(industries):
    # object that gets returned
    industry_equities = {}

    # If industries is a string, make it a list
    if isinstance(industries, str):
        industries = [industries]

    for industry in industries.keys():
        url = f"https://www.barchart.com/stocks/quotes/-{industry}/components?orderBy=weightedAlpha&orderDir=desc&page=all"
        
        # use a context manager to create and close the context and browser
        async with setup_context() as context:

            equities = await extract_data(url, context)

            if equities:
                equities = filter_equities(equities)
                industry_equities[industry] = equities

    return industry_equities



