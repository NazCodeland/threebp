import { chromium, ChromiumBrowser, ElementHandle, Page } from "playwright";
import { upload_to_db_barchart } from "./database";

const industries = [
	"VURA",
	"VPTC",
	// ... rest of the industries
];

// This function is extract rows of data from a custom element on a webpage.
// In this case, the columns are "symbol" and "name" from barchart.com
async function extractSymbolAndName(
	page: Page,
	customElement: ElementHandle<SVGElement | HTMLElement> | null
) {
	return await page.evaluate((element) => {
		// Check if the custom element exists. If not, log an error message and return.
		const shadowRoot = element
			? (element as Element).shadowRoot
			: console.log("no element", element);
		if (!shadowRoot) {
			console.log("no shadowRoot", shadowRoot);
			return;
		}

		// Select all elements with the class "set-class.row._grid_columns" from the shadow root of the custom element.
		// Map over each selected element (row) and extract the symbol and name from the appropriate cells.
		// Return an array of objects, each containing the symbol and name from a row.
		return Array.from(
			shadowRoot.querySelectorAll("set-class.row._grid_columns")
		).map((row: any) => {
			const symbol_cell = row.querySelector("div._cell.symbol text-binding");
			const symbol_name_cell = row.querySelector(
				"div._cell.symbolName text-binding"
			);
			const symbol_text = symbol_cell
				? symbol_cell.shadowRoot.textContent
				: null;
			const name_text = symbol_name_cell
				? symbol_name_cell.shadowRoot.textContent
				: null;
			return { symbol: symbol_text, name: name_text };
		});
	}, customElement);
}

// This function is designed to filter an array of row objects into two categories based on the contents of the symbol and name properties.
function filterEquities(rows: any) {
	console.log("rows", rows);

	// Filter the rows into two categories: nonEquities and equities.
	// nonEquities contains all rows where the symbol includes "-PR", "-WT", or "-PF-", or the name includes "USD".
	// equities contains all rows that do not meet the criteria for nonEquities.

	// NoteToSelf: if performance is an issue, perhaps the following would be faster with
	// a Regex pattern.
	const nonEquities = rows.filter(
		(row: any) =>
			row.symbol.includes("-PR") ||
			row.symbol.includes("-WT") ||
			row.symbol.includes("-PF-") ||
			row.name.includes("USD")
	);
	const equities = rows.filter(
		(row: any) =>
			!row.symbol.includes("-PR") &&
			!row.symbol.includes("-WT") &&
			!row.symbol.includes("-PF-") &&
			!row.name.includes("USD")
	);
	// return { equities, nonEquities };
	return { equities };
}

// This function is designed to scroll through a webpage in a browser environment.
// It's necessary because barchart data tables do not fully load until they are in the viewport.
// By scrolling to the bottom of the page, we ensure that all elements have been loaded and displayed.
async function scrollPageToBottom(page: Page) {
	return await page.evaluate(() => {
		return new Promise((resolve) => {
			let totalHeight = 0; // This variable keeps track of the total height scrolled so far.
			const distance = 100; // This is the distance that will be scrolled in each interval.

			// We use setInterval to create a loop that scrolls the page and checks if we've reached the bottom.
			const timer = setInterval(() => {
				const scrollHeight = document.body.scrollHeight; // This is the total scrollable height of the body element.
				window.scrollBy(0, distance); // This line scrolls the window by the specified distance.
				totalHeight += distance; // We add the distance scrolled to the total height.

				// If the total height scrolled is greater than or equal to the scrollable height, we've reached the bottom.
				if (totalHeight >= scrollHeight) {
					clearInterval(timer); // We clear the interval to stop the loop.
					resolve(true); // We resolve the promise with 'true' to indicate that the function has completed successfully.
				}
			}, 100); // The loop runs every 100 milliseconds.
		});
	});
}

// This function is designed to automate the process of visiting a series of webpages,
// scrolling to the bottom of each page to ensure all content is loaded, and then
// extracting and processing data from each page.
export async function extractIndustryEquities(industries: any) {
	// Launch a new browser instance.
	const browser: ChromiumBrowser = await chromium.launch({ headless: false });
	// Create a new browser context. This represents a single session of browsing activity (including cookies, localStorage, etc).
	const context = await browser.newContext();

	let industryEquities: any = {};

	// Loop over each industry in the industries array.
	for (const industry of industries) {
		// Create a new page in the browser context.
		const page: Page = await context.newPage();
		// Construct the URL for the current industry.
		const url = `https://www.barchart.com/stocks/quotes/-${industry}/components?orderBy=weightedAlpha&orderDir=desc&page=all`;
		// Navigate to the constructed URL.
		await page.goto(url);
		// Scroll to the bottom of the page to ensure all content is loaded.
		await scrollPageToBottom(page);
		// Wait for the "bc-data-grid" element to be loaded in the DOM.
		await page.waitForSelector("bc-data-grid");

		// Select the "bc-data-grid" element from the page.
		const customElement: ElementHandle<SVGElement | HTMLElement> | null =
			await page.$("bc-data-grid");
		// Extract the rows of data from the selected element.
		const rows = await extractSymbolAndName(page, customElement);

		// If rows were successfully extracted...(incase of error)
		if (rows) {
			const { equities } = filterEquities(rows);
			industryEquities[industry] = { equities };
		}

		upload_to_db_barchart(industryEquities).catch((error) => {
			console.log(error);
		});

		// Close the current page.
		await page.close();
	}

	// Close the browser once all industries have been processed.
	await browser.close();

	return industryEquities;
}
