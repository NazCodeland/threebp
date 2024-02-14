import asyncio
import json
import os
from typing import Optional
from playwright.async_api import Page, ElementHandle
from playwright.async_api import async_playwright

# Global variables to store the p, browser, and context objects
p = None
browser = None
context = None

async def _save_cookies():
    cookies = await context.cookies()
    with open('cookies.json', 'w') as f:
        json.dump(cookies, f)

async def _load_cookies():
    if os.path.exists('cookies.json'):
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        await context.addCookies(cookies)

# A helper function to create and assign p, context, and browser
async def _start_context():
    """
    This function creates and assigns a Playwright object, a browser instance, and a context object to the global variables.
    The function does not close these objects automatically, so you need to close them manually when you are done with them.
    """
    global p, browser, context # Declare the global variables
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context()

# A helper function to close the p, browser, and context objects
async def _stop_context():
    """
    This function closes the Playwright object, the browser instance, and the context object.
    """
    global p, browser, context # Declare the global variables
    await context.close()
    await browser.close()
    await p.stop()

async def extract_data(page: Page, custom_element: Optional[ElementHandle], url) -> list:
    return await page.evaluate("""({custom_element, url}) => {
        
        const shadowRoot = custom_element ? custom_element.shadowRoot : console.log("no element", custom_element);
        if (!shadowRoot) {
            console.log("no shadowRoot", shadowRoot);
            return;
        }

        // the sectors and industries page contain only symbol and sector/industry (symbol_name) information
        function extract_symbol_and_symbol_name(){
            return Array.from(shadowRoot.querySelectorAll("set-class.row._grid_columns")).map((row) => {
                const symbol_cell = row.querySelector("div._cell.symbol text-binding");
                const symbol_name_cell = row.querySelector("div._cell.symbolName text-binding");

                const symbol_text = symbol_cell ? symbol_cell.shadowRoot.textContent : null;
                const symbol_name_text = symbol_name_cell ? symbol_name_cell.shadowRoot.textContent : null;

                return { symbol: symbol_text, symbol_name: symbol_name_text }        
            });
        }

        // the industry equity page contains symbol and all the following information
        function extract_equity_symbol_and_financials(){
            return Array.from(shadowRoot.querySelectorAll("set-class.row._grid_columns")).map((row) => {
                const symbol_cell = row.querySelector("div._cell.symbol text-binding");
                const marketCapitalization = row.querySelector("div._cell._align_right.marketCap text-binding");

                // Quarter information
                const revenueLastQuarter = row.querySelector("div._cell._align_right.revenueLastQuarter text-binding");
                const revenueGrowthLastQuarter = row.querySelector("div._cell._align_right.revenueGrowthLastQuarter text-binding");
                const revenueGrowth1qAgo = row.querySelector("div._cell._align_right.revenueGrowth1qAgo text-binding");
                const revenueGrowth2qAgo = row.querySelector("div._cell._align_right.revenueGrowth2qAgo text-binding");
                const grossProfitLastQuarter = row.querySelector("div._cell._align_right.grossProfitLastQuarter text-binding");
                const operatingIncomeLastQuarter = row.querySelector("div._cell._align_right.operatingIncomeLastQuarter text-binding");
                const netIncomeLastQuarter = row.querySelector("div._cell._align_right.netIncomeLastQuarter text-binding");

                // Annual information
                const revenueLastYear = row.querySelector("div._cell._align_right.revenueLastYear text-binding");
                const revenueGrowthLastYear = row.querySelector("div._cell._align_right.revenueGrowthLastYear text-binding");
                const revenueGrowth1yAgo = row.querySelector("div._cell._align_right.revenueGrowth1yAgo text-binding");
                const revenueGrowth2yAgo = row.querySelector("div._cell._align_right.revenueGrowth2yAgo text-binding");
                const grossProfitLastYear = row.querySelector("div._cell._align_right.grossProfitLastYear text-binding");
                const operatingIncomeLastYear = row.querySelector("div._cell._align_right.operatingIncomeLastYear text-binding");

                const symbol_text = symbol_cell ? symbol_cell.shadowRoot.textContent : null;
                const marketCap = marketCapitalization ? marketCapitalization.shadowRoot.textContent : null;

                // Quarter information
                const revLastQ = revenueLastQuarter ? revenueLastQuarter.shadowRoot.textContent : null;
                const revGrowthLastQ = revenueGrowthLastQuarter ? revenueGrowthLastQuarter.shadowRoot.textContent : null;
                const revGrowth1qAgo = revenueGrowth1qAgo ? revenueGrowth1qAgo.shadowRoot.textContent : null;
                const revGrowth2qAgo = revenueGrowth2qAgo ? revenueGrowth2qAgo.shadowRoot.textContent : null;
                const grossProfitLastQ = grossProfitLastQuarter ? grossProfitLastQuarter.shadowRoot.textContent : null;
                const operatingIncomeLastQ = operatingIncomeLastQuarter ? operatingIncomeLastQuarter.shadowRoot.textContent : null;
                const netIncomeLastQ = netIncomeLastQuarter ? netIncomeLastQuarter.shadowRoot.textContent : null;

                // Annual information
                const revLastY = revenueLastYear ? revenueLastYear.shadowRoot.textContent : null;
                const revGrowthLastY = revenueGrowthLastYear ? revenueGrowthLastYear.shadowRoot.textContent : null;
                const revGrowth1yAgo = revenueGrowth1yAgo ? revenueGrowth1yAgo.shadowRoot.textContent : null;
                const revGrowth2yAgo = revenueGrowth2yAgo ? revenueGrowth2yAgo.shadowRoot.textContent : null;
                const grossProfitLastY = grossProfitLastYear ? grossProfitLastYear.shadowRoot.textContent : null;
                const operatingIncomeLastY = operatingIncomeLastYear ? operatingIncomeLastYear.shadowRoot.textContent : null;

                return {
                    equity_symbol: symbol_text,
                    revLastQ,revGrowthLastQ,                    
                    revGrowth1qAgo,                    
                    revGrowth2qAgo,                    
                    grossProfitLastQ,                    
                    operatingIncomeLastQ,                    
                    netIncomeLastQ,                    
                    revLastY,                    
                    revGrowthLastY,                    
                    revGrowth1yAgo,                    
                    revGrowth2yAgo,                    
                    grossProfitLastY,                    
                    operatingIncomeLastY 
                };
            });
        }

        // sector (indices) and industries
        if(url.includes('indices') || url.includes('industry')){
            return extract_symbol_and_symbol_name()
        }
        else {
            return extract_equity_symbol_and_financials()
        }
    }""", {"custom_element": custom_element, "url":url})

async def _login():
    page = await context.new_page()
    await page.goto('https://www.barchart.com/login')

    # Fill in the email and password fields
    await page.fill('input[name="email"]', 'investingclarity@gmail.com')
    await page.fill('input[name="password"]', 'NewInvestLife10')

    # Click the login button
    await page.click('.bc-button.login-button')

    await _save_cookies()
    await page.close()

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

async def navigate_and_prepare_page(context, url, page: Optional[Page] = None):
    page = await context.new_page()
    await page.goto(url)
    
    
    if 'industry' in url:
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
    
    await scroll_page_to_bottom(page)
    await page.wait_for_selector("bc-data-grid")
    
    return page

async def extract_data_from_page(page: Page, url:str):
    custom_element = await page.query_selector("bc-data-grid")
    rows = await extract_data(page, custom_element, url)
    await page.close()
    return rows


async def extract_sectors():
    url = "https://www.barchart.com/search?q=$TT&regions=ca&assets=indices"
    page = await navigate_and_prepare_page(context, url)
    sectors = await extract_data_from_page(page, url)
    sectors = list(map(lambda d: {'sector_symbol': d['symbol'], 'sector_name': d['symbol_name']}, sectors))
    return sectors if sectors else []

async def extract_industries():
    url = "https://www.barchart.com/ca/stocks/sectors/industry-performance?orderBy=priceChange&orderDir=desc"
    page = await navigate_and_prepare_page(context, url)
    industries = await extract_data_from_page(page, url)
    industries = list(map(lambda d: {'industry_symbol': d['symbol'], 'industry_name': d['symbol_name']}, industries))
    return industries if industries else []

async def extract_industry_equities(industries):
    if isinstance(industries, str):
        industries = [industries]

    industry_equities = []
    for industry_data in industries:
        industry = industry_data['industry_symbol'].lstrip('-')
        url = f"https://www.barchart.com/stocks/quotes/-{industry}/components?orderBy=weightedAlpha&orderDir=desc&page=all"
        page = await navigate_and_prepare_page(context, url)
        equities = await extract_data_from_page(page, url)

        if equities:
            for equity in equities:
                equity['industry_symbol'] = industry
                industry_equities.append(equity)

    return industry_equities



