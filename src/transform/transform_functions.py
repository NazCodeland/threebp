from typing import List, Dict

def filter_rows(rows: List[Dict]) -> List[Dict]:
    # This line creates a list of invalid symbols. It checks each row in the input list 'rows' and includes it in 'invalid_symbols' if the symbol contains "-PR", "-WT", "-PF-", or if the symbol name contains "USD".
    invalid_symbols = [row for row in rows if "-PR" in row['symbol'] or "-WT" in row['symbol'] or "-PF-" in row['symbol'] or "USD" in row['name']]
    
    # This line creates a list of valid symbols. It checks each row in the input list 'rows' and includes it in 'valid_symbols' if the symbol does not contain "-PR", "-WT", "-PF-", "-B", "USD", or "Cl B".
    # It also modifies the symbol in each row based on certain conditions:
    # - If the symbol ends with '.VN', it replaces '.VN' with '.V'.
    # - If the symbol starts with '$', it removes the '$'.
    # - If the symbol starts with '-', it removes the '-'.
    valid_symbols = [dict(row, symbol=row['symbol'].replace('.VN', '.V')) if row['symbol'].endswith('.VN') else dict(row, symbol=row['symbol'].replace('$', '')) if row['symbol'].startswith('$') else dict(row, symbol=row['symbol'].lstrip('-')) if row['symbol'].startswith('-') else row for row in rows if not any(substring in row['symbol'] for substring in ["-PR", "-WT", "-PF-", "-B"]) and "USD" not in row['name'] and "Cl B" not in row['name']]
    
    # The function returns the list of valid symbols.
    return valid_symbols
