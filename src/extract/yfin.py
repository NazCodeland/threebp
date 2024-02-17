import math
from typing import Any, Dict, List
import time
import concurrent.futures
from utilities import save_dataframe, save_to_html_and_open
import pandas as pd

import requests
import yfinance as yf
from yfinance.data import YfData
from yfinance.scrapers.fundamentals import Fundamentals

# PRICE-DATA API LINK
# https://query2.finance.yahoo.com/v8/finance/chart/MNS.TO?1509744000&1668748800&interval=1d&range=1mo&includePrePost=False
def download_price(symbols: list[str], intervals: dict[str, str], market_hours=False) -> pd.DataFrame:
    """
    Downloads OHLCV data for the given symbols and intervals.

    Parameters:
    symbols (list[str]): List of symbols to download data for.
    intervals (dict[str, str]): Dictionary mapping interval names to periods.
    market_hours (bool): Whether to only include market hours. Defaults to False.

    Returns:
    pd.DataFrame: A DataFrame with the following columns for each symbol:
        - 'open'
        - 'high'
        - 'low'
        - 'close'
        - 'volume'
    The DataFrame has a MultiIndex with the following levels:
        - 'date'
        - 'interval'
    """
    
    dfs = []
    for interval in intervals.keys():
        print('-------------------------------------')
        print("downloading data for:", interval)
        print('-------------------------------------')
        period = intervals[interval]
        start_time = time.time()
        try:
            if market_hours:
                start = intervals[interval]['start']
                end = intervals[interval]['end']
                df = yf.download(symbols, start=start, end=end, interval=interval, rounding=True, group_by='ticker', ignore_tz=True, keepna=True)

            else:
                df = yf.download(symbols, period=period, interval=interval, rounding=True, group_by='ticker', ignore_tz=True, keepna=True)
                # df = yf.download(symbols, start=intervals[interval]['start'], end=intervals[interval]['end'], interval=interval, rounding=True, group_by='ticker', ignore_tz=True, keepna=True)
                # df = df.tail(5)
                
            df = df.drop(columns='Adj Close', level=1)  # Remove 'Adj Close' column
            df.columns = df.columns.set_levels(df.columns.levels[1].str.lower(), level=1)  # Make column names lowercase
            df = df.assign(interval=interval)  # Add interval column
            df.set_index([pd.Index(df.index, name='date'), 'interval'], inplace=True)  # Set Interval as part of the index with column names
            dfs.append(df)

        except Exception as e:
            print(f"Failed to download data for symbols {symbols}, interval {interval}. Error: {e}")
            
        end_time = time.time()  # End the timer
        print(f"Time taken to download data for interval {interval}: {end_time - start_time} seconds")

    
    if not market_hours:
        df_all = pd.concat(dfs)
        return df_all
    else:
        return df


# FUNDAMENTALS API LINK:
# https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/ERO.TO?symbol=ERO.TO&type=quarterlyTotalRevenue,quarterlyCostOfRevenue,quarterlyGrossProfit&period1=1451520000&period2=1705564800
# C:\Users\o0\source\projects\mine\python\threebp\env\Lib\site-packages\yfinance\const.py

# def download_financials_for_symbol(symbol:str):
#     symbol_data = yf.Ticker(symbol)
#     quarterly_financials = symbol_data.quarterly_income_stmt
#     quarterly_financials = quarterly_financials.iloc[::-1]
#     print(quarterly_financials)
#     return quarterly_financials
    

keys = ["TotalRevenue", "CostOfRevenue", "GrossProfit", 
        "PretaxIncome", "NetIncome", "CreditLossesProvision"]
keys = [
	"TaxEffectOfUnusualItems",
	"TaxRateForCalcs",
	"NormalizedEBITDA",
	"NormalizedDilutedEPS",
	"NormalizedBasicEPS",
	"TotalUnusualItems",
	"TotalUnusualItemsExcludingGoodwill",
	"NetIncomeFromContinuingOperationNetMinorityInterest",
	"ReconciledDepreciation",
	"ReconciledCostOfRevenue",
	"EBITDA",
	"EBIT",
	"NetInterestIncome",
	"InterestExpense",
	"InterestIncome",
	"ContinuingAndDiscontinuedDilutedEPS",
	"ContinuingAndDiscontinuedBasicEPS",
	"NormalizedIncome",
	"NetIncomeFromContinuingAndDiscontinuedOperation",
	"TotalExpenses",
	"RentExpenseSupplemental",
	"ReportedNormalizedDilutedEPS",
	"ReportedNormalizedBasicEPS",
	"TotalOperatingIncomeAsReported",
	"DividendPerShare",
	"DilutedAverageShares",
	"BasicAverageShares",
	"DilutedEPS",
	"DilutedEPSOtherGainsLosses",
	"TaxLossCarryforwardDilutedEPS",
	"DilutedAccountingChange",
	"DilutedExtraordinary",
	"DilutedDiscontinuousOperations",
	"DilutedContinuousOperations",
	"BasicEPS",
	"BasicEPSOtherGainsLosses",
	"TaxLossCarryforwardBasicEPS",
	"BasicAccountingChange",
	"BasicExtraordinary",
	"BasicDiscontinuousOperations",
	"BasicContinuousOperations",
	"DilutedNIAvailtoComStockholders",
	"AverageDilutionEarnings",
	"NetIncomeCommonStockholders",
	"OtherunderPreferredStockDividend",
	"PreferredStockDividends",
	"NetIncome",
	"MinorityInterests",
	"NetIncomeIncludingNoncontrollingInterests",
	"NetIncomeFromTaxLossCarryforward",
	"NetIncomeExtraordinary",
	"NetIncomeDiscontinuousOperations",
	"NetIncomeContinuousOperations",
	"EarningsFromEquityInterestNetOfTax",
	"TaxProvision",
	"PretaxIncome",
	"OtherIncomeExpense",
	"OtherNonOperatingIncomeExpenses",
	"SpecialIncomeCharges",
	"GainOnSaleOfPPE",
	"GainOnSaleOfBusiness",
	"OtherSpecialCharges",
	"WriteOff",
	"ImpairmentOfCapitalAssets",
	"RestructuringAndMergernAcquisition",
	"SecuritiesAmortization",
	"EarningsFromEquityInterest",
	"GainOnSaleOfSecurity",
	"NetNonOperatingInterestIncomeExpense",
	"TotalOtherFinanceCost",
	"InterestExpenseNonOperating",
	"InterestIncomeNonOperating",
	"OperatingIncome",
	"OperatingExpense",
	"OtherOperatingExpenses",
	"OtherTaxes",
	"ProvisionForDoubtfulAccounts",
	"DepreciationAmortizationDepletionIncomeStatement",
	"DepletionIncomeStatement",
	"DepreciationAndAmortizationInIncomeStatement",
	"Amortization",
	"AmortizationOfIntangiblesIncomeStatement",
	"DepreciationIncomeStatement",
	"ResearchAndDevelopment",
	"SellingGeneralAndAdministration",
	"SellingAndMarketingExpense",
	"GeneralAndAdministrativeExpense",
	"OtherGandA",
	"InsuranceAndClaims",
	"RentAndLandingFees",
	"SalariesAndWages",
	"GrossProfit",
	"CostOfRevenue",
	"TotalRevenue",
	"ExciseTaxes",
	"OperatingRevenue"
]

def download_financials_for_symbol(symbol:str, period:str):
    session = requests.Session()
    
    fundamentals = Fundamentals(YfData(session), symbol)
    financials = fundamentals.financials  # Get the Financials object
    # Fetch the financials time series data for the specified keys
    financials_data = financials.get_financials_time_series(period, keys)
    print(financials_data)

    financials_data.index.name = 'line item'
    financials_data.reset_index(inplace=True)
    financials_data.insert(0, 'symbol', symbol)

    return financials_data


def download_financials(symbols: List[str], period:str) -> List[Dict['str', Dict['str', Any]]]:
    all_financials = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_symbol = {executor.submit(download_financials_for_symbol, symbol, period): symbol for symbol in symbols}
        
        for future in concurrent.futures.as_completed(future_to_symbol):
            symbol = future_to_symbol[future]    
            try:
                financials = future.result()
                all_financials.append(financials )

            except Exception as exc:
                print(f'{symbol} generated an exception: {exc}')
    
    all_financials_df = pd.concat(all_financials)
    return all_financials_df








