

def convert_to_yearly(df):
    # Convert 'Date' column to datetime and set it as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Separate the symbol and timeframe
    df[['symbol', 'timeframe']] = df['symbol'].str.split('_', expand=True)

    # Resample to yearly data
    df_yearly = df.groupby('symbol').resample('Y').agg(
        {
            'Open': 'first', 
            'High': 'max', 
            'Low': 'min', 
            'Close': 'last',
            'Volume': 'sum'
        }
    )

    return df_yearly

# df_yearly = convert_to_yearly(df)
