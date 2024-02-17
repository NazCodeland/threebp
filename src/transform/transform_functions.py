
import io
import pandas as pd
from typing import List, Dict, Tuple

from utilities import save_to_html_and_open

def sanitize_data(data):
    # Read the string 'data' as a CSV file into a pandas DataFrame
    df = pd.read_csv(io.StringIO(data))
    # Reverse the order of the DataFrame rows
    # df = df.iloc[::-1]
    # delete the "Adj Close" column from the DataFrame
    sanitized_df = df.drop(columns=["Adj Close"])
    # Round all cells in the DataFrame to 2 decimal places
    sanitized_df = sanitized_df.round(2)
    # Reverse the DataFrame
    # sanitized_df = sanitized_df.iloc[::-1]
    
    return sanitized_df

def filter_data(financial_objects: List[Dict]) -> List[Dict]:
    exclude_sectors = ["TTGD"]
    exclude_industries = [
        "VTXS", "VTOP", "VBOT", "VCMP", "VTHC", "VTTS", "VTMT", "VTRE", "VTTK", "VTIN", "VTFS", "VTCD", "VTUT", "VTCS", "VTEN"]

    # warrants, preferred shares, indices, top or bottom 100 stocks, etc...
    exclude_substring_symbols = ["-PR", "-WT", "-PF-", ".NE"]
    exclude_symbols = [
        "SPPP.TO", "CLP-UN.TO", "MNS.TO", "MNT.TO", "TECK-A.TO", "ACRG-B-U.CN", "RET.VN", "GCG-A.TO", "URB.TO", "TCL-B.TO", "ADW-B.TO", "CSW-B.TO",
        "RAY-B.TO", "BBD-A.TO", "QBR-A.TO", "RCI-A.TO", "AKT-B.TO", "JET-B.NE", "CTC"]

    valid_symbols = []
    invalid_symbols = []

    keys_to_check = ['sectorSym', 'industrySym', 'symbol']
    for fin_object in financial_objects:
        excluded = False

        for key in keys_to_check:
            if key in fin_object:
                modified_value = fin_object[key]
                if modified_value.endswith('.VN'):
                    modified_value = modified_value.replace('.VN', '.V')
                if modified_value.startswith('$'):
                    modified_value = modified_value.replace('$', '')
                if modified_value.startswith('-'):
                    modified_value = modified_value.lstrip('-')
                if modified_value == 'ACRG-A-U.CN':
                    modified_value = 'ACRG-AU.CN'

                sectors_excluded = modified_value in exclude_sectors
                industries_excluded = modified_value in exclude_industries
                symbols_excluded = any(substring in modified_value for substring in exclude_substring_symbols) or modified_value in exclude_symbols

                if sectors_excluded or industries_excluded or symbols_excluded:
                    excluded = True
                    break  # if the modified_value is excluded, no need to check other keys for the same fin_object
                else:
                    fin_object[key] = modified_value  # update the key in the new fin_object

        if excluded:
            invalid_symbols.append(fin_object)
        else:
            valid_symbols.append(fin_object)

    return valid_symbols

def wide_to_long(df):
    # this function collapses a MultiIndex from 'wide' format to 'long' format

    # The stack() function is used to "compress" a level in the DataFrame's columns.
    # This transforms the DataFrame from a wide format to a long format.
    # The reset_index() function is then used to reset the index of the DataFrame.
    # This results in a DataFrame where each row represents a single observation for a symbol at a given time.
    # The rename() function is used to rename the 'level_2' column to 'symbol'.
    df = df.stack(level=0).reset_index().rename(columns={'level_2': 'symbol'})
    return df

def add_year_interval(df):
    # Set 'date', 'symbol', and 'interval' as indices
	df.set_index(['date', 'symbol', 'interval'], inplace=True)
	
    # Define the aggregation dictionary for resampling
	agg_dict = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume':'sum'}
	
    # Group the DataFrame by 'symbol' and 'interval' indices, filter for 1-month intervals, and resample to 1-year intervals
	df_yearly = df[df.index.get_level_values('interval') == '1mo'].groupby(level=['symbol', 'interval']).resample('Y', level='date').agg(agg_dict)
	
    # Reset the index of the DataFrame
	df_yearly.reset_index(inplace=True)
	
    # Add the 'interval' column back to the DataFrame
	df_yearly['interval'] = '1y'
	
	# Reset the index of the original DataFrame
	df.reset_index(inplace=True)
	
    # Concatenate the original DataFrame and the resampled DataFrame
	df = pd.concat([df, df_yearly])
    
	return df 

def tail_by_group(df):
    df = df.groupby(['symbol', 'interval']).apply(lambda x: x.tail(5)).reset_index(drop=True)
    return df

def categorize_interval_and_sort_data(df_all):

    # This line is converting the 'interval' column to a categorical data type with the specified categories and order.
    # The categories are '1m', '5m', '60m', '1d', '1wk', '1mo' and they are ordered. 
    # This means that they can be sorted or compared according to the order specified, which is useful for ordinal data.
    # df_all['interval'] = pd.Categorical(df_all['interval'], categories=['1y', '1mo', '1wk', '1d', '60m', '5m', '1m'], ordered=True)
    df_all['interval'] = pd.Categorical(df_all['interval'], categories=['1y', '1mo', '1wk', '1d', '60m'], ordered=True)

    # This will sort the DataFrame in the following way:
    # 1. 'symbol' in ascending order: This means the symbols will be sorted from A to Z.
    # 2. For each group of rows with the same symbol, 'interval' will be sorted in ascending order.
    # 3. For each group of rows with the same symbol and interval, 'date' will be sorted in descending order. 
    # This means the most recent dates will come first.
    df_all = df_all.sort_values(by=['symbol', 'interval', 'date'], ascending=[True, True, False])

    # re-order the columns from: ['date', 'interval', 'symbol', 'close', 'high', 'low', 'open', 'volume'] to:
    df_all = df_all.reindex(columns=['date', 'interval', 'symbol', 'open', 'high', 'low', 'close', 'volume'])

    return df_all

def merge_price_with_financials(threebp_df: pd.DataFrame, financials_df: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(threebp_df, financials_df, on='symbol', how='outer')
    return merged_df

def transform_financials(financial_data: pd.DataFrame) -> pd.DataFrame:    
    def vertical_analysis(financial_data: pd.DataFrame) -> pd.DataFrame:
        # Reshape the DataFrame to multi-index format
        financial_data_multi = financial_data.set_index(['symbol', 'line item']).stack()

        # Convert the financial values to numeric format
        financial_data_multi = financial_data_multi.apply(pd.to_numeric, errors='coerce')

        # Calculate the ratios of all line items against the 'TotalRevenue' for each symbol
        financial_data_ratio = financial_data_multi.div(financial_data_multi.xs('TotalRevenue', level='line item'))
        print(financial_data_ratio.unstack())
        return financial_data_ratio.unstack()
    
    vertical_analysis(financial_data)



    # # Clean up and convert the following columns to numeric type
    # columns = ['revLastQ', 'grossPLastQ', 'opIncLastQ', 'netIncLastQ', 'revLastY', 'grossPLastY', 'opIncLastY']
    # financials_df = financials_df.replace('0', '')
    # # financials_df[columns] = financials_df[columns].replace(',', '', regex=True).apply(pd.to_numeric, errors='coerce')

    # # Calculate new values for the following columns' and overwrite the original columns
    # # Quarterly
    # financials_df['grossPGLastQ'] = round(financials_df['grossPLastQ'] / financials_df['revLastQ'], 2)
    # financials_df['opIncGLastQ'] = round(financials_df['opIncLastQ'] / financials_df['revLastQ'], 2)
    # financials_df['netIncGLastQ'] = round(financials_df['netIncLastQ'] / financials_df['revLastQ'], 2)

    # # Annually
    # financials_df['grossPGLastY'] = round(financials_df['grossPLastY'] / financials_df['revLastY'], 2)
    # financials_df['opIncGLastY'] = round(financials_df['opIncLastY'] / financials_df['revLastY'], 2)

    
    # # Reorder the columns to maintain the original order
    # financials_df = financials_df[[
    #     'symbol', 'marketCap', 'revGLastQ', 'revG1qAgo', 'revG2qAgo', 'grossPGLastQ', 'opIncGLastQ', 
    #     'netIncGLastQ', 'revGLastY', 'revG1yAgo', 'revG2yAgo', 'grossPGLastY', 'opIncGLastY', 'industrySym'
    #     ]]

    # return financial_df




# def transform_financials(financials_data):
#     data_list = []

#     for financials in financials_data:
#         for symbol, records in financials.items():
#             for date, record in records.items():
#                 # Flatten the data and append it to the list
#                 for item, value in record.items():
#                         data_list.append([symbol, date, item, value])

#         # Convert the list into a DataFrame
#         df = pd.DataFrame(data_list, columns=['symbol', 'date', 'line item', 'value'])

#         # Convert the 'Date' and 'Line Item' columns to a Categorical data type with the original order
#         df['date'] = pd.Categorical(df['date'], categories=df['date'].unique(), ordered=True)
#         df['line item'] = pd.Categorical(df['line item'], categories=df['line item'].unique(), ordered=True)

#         # Pivot the DataFrame
#         pivot_df = df.pivot(index=['symbol', 'line item'], columns='date', values='value')

#         # Reset the index
#         pivot_df.reset_index(inplace=True)

#         # Save to HTML and open
#         save_to_html_and_open(pivot_df)
#         return pivot_df
    


