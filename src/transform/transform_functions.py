
import io
import pandas as pd
from typing import List, Dict
import webbrowser
import os
import datetime


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
    exclude_substring_symbols = ["-PR", "-WT", "-PF-"]
    exclude_symbols = [
        "TECK-A.TO", "ACRG-B-U.CN", "RET.VN", "GCG-A.TO", "URB.TO", "TCL-B.TO", "ADW-B.TO", "CSW-B.TO",
        "RAY-B.TO", "BBD-A.TO", "QBR-A.TO", "RCI-A.TO", "AKT-B.TO", "JET-B.NE", "CTC"]

    valid_symbols = []
    invalid_symbols = []

    keys_to_check = ['sector_symbol', 'industry_symbol', 'equity_symbol']
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






def save_to_html_and_open(df):
    # Get the current date and time
    now = datetime.datetime.now()
    
    # Format it as a string with milliseconds and microseconds
    timestamp = now.strftime("%Y%m%d%H%M%S%f")
    
    # Use the timestamp to create a unique filename
    filename = f"data_{timestamp}.html"

    with open(filename, "w") as f:
        f.write(df.to_html(escape=False))
    
    webbrowser.open('file://' + os.path.realpath(filename))
