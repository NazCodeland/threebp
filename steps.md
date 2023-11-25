## Data Collection, Data Cleaning, and Data Transformations

> **Data Collection** is the process of obtaining the data that is needed for a specific purpose. This can be done by accessing various sources, such as files, databases, or web pages.

> **Data Cleaning** is the process of ensuring that the data is of high quality and suitable for analysis. This can involve removing or correcting missing, incorrect, or irrelevant data, as well as checking for errors or inconsistencies.

> **Data Transformation** is the process of converting the data into a format that is easier to understand and work with. This can involve applying various operations, such as normalizing, encoding, or creating new variables, to the data.

> The steps below, each task, fall under the data collection, data cleaning, and data transformation categories defined above.

### Sectors data from barchart

1. Manually created list (this needs to be automated)
2. Clean data (gathered manually - this should be automated)
3. Upload to SQL Database
4. Download from SQL Database
5. Transform data into Pandas Dataframe
   1. The DataFrame columns will be "Open", "High", "Low", "Close", and "Volume".
      The values will be the aggregate grouped OHLCV of its constituents (industries)

### Industry data from Barchart

1. Download data (scrape barchart for all industry names and their symbols)
2. Clean data (gathered manually - this should be automated)
3. Upload to SQL Database
4. Download from SQL Database
5. Transform data into Pandas Dataframe
   1. The DataFrame columns will be "Open", "High", "Low", "Close", and "Volume".
      The values will be the aggregate grouped OHLCV of its constituents (equities)

### Industry Equities from Barchart

1. Download data (scrape barchart for equities in each industry)
2. Clean data (Filter Barchart.com/ca Equities for each Industry from Non-Equity symbols
   (non-TSX based equities, warrants, preferred shares etc))
3. Upload to SQL Database
4. Download from SQL Database
5. Transform data into Pandas Dataframe
   1. The DataFrame columns will be "Open", "High", "Low", "Close", and "Volume".
      The values will be the OHLCV for the stock

### Equities data (OHLCV) from Yahoo

1. Download data (For each symbol, for different timeframes, download OHLCV)
2. Clean data (Reverse Yahoo DataFrame from ascending to descending order)
3. Upload to SQL Database
4. Download from SQL Database
5. Transform data into Pandas Dataframe
   1. The DataFrame columns will be "Open", "High", "Low", "Close", and "Volume".
      The values will be the OHLCV for the stock
   2. Create various TimeFrame DataFrames out of the available timeframes. For example,
      create Yearly DataFrames for equities and and also, the TimeFrames for all Industries/Sectors/Exchanges
   3. Create TSX Instance
   4. For "TSX.sectors", "TSX.industries" add their respective DataFrames including the Sectors different TimeFrame DataFrames.
   5. For each industry in "TSX.industries", add industry equities including the Industries different TimeFrame DataFrames

TSX

- sector_one

  - industries_one

    - stocks_one
    - stock_two

  - industry_two
    - stock_one
    - stock_two

- sector_two

  - industries_one

    - stocks_one
    - stock_two

  - industry_two
    - stock_one
    - stock_two

---

## Business Logic

>

TSX.sectors = { "sector": ["industry_one", "industry_two", "industry_three"] }
TSX.industries = { "industry": ["symbol_one", "symbol_two", "symbol_three"] }

symbol_one = df
df = OHLCV columns

<!-- Note to self: Tracking and viewing a whole industry indirectly improves the odds
                  of threebp. If I am correct about this assertion, I think it improves the odds because, If the whole industry in a bullish 3bp, by definition of averages - some will gain more than others. The opposite is true in a bearish 3bp. Therefore, I think, this ends up being a net positive for
                  the whole probability of the whole system: threebp, risk management, HA, etc..
                  - At the end of the day, if you took 2 trades, one had a continuation in
                  trend and the other didn't and went and broke the trend from 3bp. Then
                  you will make more money than your losing trade if you follow the rules.
