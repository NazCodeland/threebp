
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



# List of substrings to exclude from the 'symbol' 
# warrants, preferred shares etc...

# warrants, preferred shares, illiquid symbols if it's a "*-A.*" or "*-B.*" etc...
excluded_symbols = [
    "-PR", "-WT", "-PF-", "-A", "TTGD", "VTXS", "VTOP", "VBOT", "VCMP", "VTHC", "VTTS", "VTMT", "VTRE", "VTTK", "VTIN", "VTFS", "VTCD", "VTUT", "VTCS", "VTEN",
    "TECK-A.TO", "TCL-B.TO", "ADW-B.TO", "CSW-B.TO", "RAY-B.TO", "BBD-A.TO", "QBR-A.TO", "RCI-A.TO", "AKT-B.TO"
    ]

# List of industry codes to exclude
excluded_industries = ["VTXS", "VTOP", "VBOT", "VCMP", "VTHC", "VTTS", "VTMT", "VTRE", "VTTK", "VTIN", "VTFS", "VTCD", "VTUT", "VTCS", "VTEN"]

def filter_rows(rows: List[Dict]) -> List[Dict]:
    # Initialize lists to hold valid and invalid symbols
    valid_symbols = []
    invalid_symbols = []

    # Iterate over each row
    for row in rows:
        # Check if the 'industry' key exists and if it's in the excluded industries list
        industry_excluded = 'industry' in row and row['industry'] in excluded_industries

        # Check if the symbol contains any excluded substrings
        symbol_excluded = any(substring in row['symbol'] for substring in excluded_symbols)
        
        if industry_excluded or symbol_excluded:
            # If so, add to the invalid symbols list
            invalid_symbols.append(row)
        else:
            # If not, process the symbol and add to the valid symbols list
            new_symbol = row['symbol']
            if new_symbol.endswith('.VN'):
                new_symbol = new_symbol.replace('.VN', '.V')
            if new_symbol.startswith('$'):
                new_symbol = new_symbol.replace('$', '')
            if new_symbol.startswith('-'):
                new_symbol = new_symbol.lstrip('-')
            valid_symbols.append(dict(row, symbol=new_symbol))

    # Return both lists
    # return valid_symbols, invalid_symbols
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
