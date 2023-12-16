from typing import Optional
from playwright.async_api import Page, ElementHandle
from playwright.async_api import async_playwright

# Global variables to store the p, browser, and context objects
p = None
browser = None
context = None

# A helper function to create and assign p, context, and browser
async def start_context():
    """
    This function creates and assigns a Playwright object, a browser instance, and a context object to the global variables.
    The function does not close these objects automatically, so you need to close them manually when you are done with them.
    """
    global p, browser, context # Declare the global variables
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context()

# A helper function to close the p, browser, and context objects
async def stop_context():
    """
    This function closes the Playwright object, the browser instance, and the context object.
    """
    global p, browser, context # Declare the global variables
    await context.close()
    await browser.close()
    await p.stop()

async def extract_rows(page: Page, custom_element: Optional[ElementHandle]) -> list:
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
            return { symbol: symbol_text, name: company_name_text };
        });
    }""", custom_element)

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

async def extract_data(url, context, page: Optional[Page] = None):
    if page is None:
        page = await context.new_page()
        await page.goto(url)
    await scroll_page_to_bottom(page)
    await page.wait_for_selector("bc-data-grid")

    custom_element = await page.query_selector("bc-data-grid")
    rows = await extract_rows(page, custom_element)

    await page.close()

    return rows

async def extract_sectors():
    url = "https://www.barchart.com/search?q=$TT&regions=ca&assets=indices"
    rows = await extract_data(url, context)
    return rows if rows else []

async def extract_industries():
    url = "https://www.barchart.com/ca/stocks/sectors/industry-performance?orderBy=priceChange&orderDir=desc"
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
    return rows if rows else []

async def extract_industry_equities(industries):
    if isinstance(industries, str):
        industries = [industries]

    industry_equities = []
    for industry_data in industries:
            industry = industry_data['symbol'].lstrip('-')
            url = f"https://www.barchart.com/stocks/quotes/-{industry}/components?orderBy=weightedAlpha&orderDir=desc&page=all"
            equities = await extract_data(url, context)
            if equities:
                for equity in equities:
                    equity['industry'] = industry
                    industry_equities.append(equity)

    return industry_equities



