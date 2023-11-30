import webbrowser
import os
import pandas as pd
import numpy as np



def check_for_buy_conditions(df):
    # all these variables return either a DataFrame or a Series for the whole df or column(s)

    # conditions for a bullish 3bp
    higher_high = df['High'] > df['High'].shift(-2)
    higher_close = df['Close'] > df['Close'].shift(-1)
    bullish_3bp = higher_high & higher_close

    # setting up columns for bearish 3bp marks
    lower_low = df['Low'] < df['Low'].shift(-2)
    lower_close = df['Close'] < df['Close'].shift(-1)

    # gain or loss from last bars close
    gain_or_loss = ((df['Close'] - df['Close'].shift(-1)) * 100) / df['Close'].shift(-1)


    # Add the new columns
    for col in ['1M', '1W', '1D']:
        df[col] = np.where(bullish_3bp, df['gain_or_loss'], df['threebp_gain_needed'])
        
    # if not in a bullish 3bp, calculate gain needed from current price to form a bullish 3bp
    threebp_highmark = np.maximum(df['Close'].shift(-1), df['High'].shift(-2))
    threebp_gain_needed = -((threebp_highmark - df['Close']) * 100) / df['Close']

    # For rows where 'gain_or_loss' is greater than or equal to 0, set the 'gain_or_loss'
    # column to the corresponding value in 'gain_or_loss'
    df.loc[gain_or_loss >= 0, 'gain_or_loss'] = gain_or_loss
    # For rows where 'gain_or_loss' is less than 0, set the 'gain_or_loss' column to NaN
    df.loc[gain_or_loss < 0, 'gain_or_loss'] = float('nan')
    # For rows where 'gain_or_loss' is greater than or equal to 0, set the 'threebp_gain_needed'
    # column to NaN
    df.loc[gain_or_loss >= 0, 'threebp_gain_needed'] = float('nan')
    # For rows where 'gain_or_loss' is less than 0, set the 'threebp_gain_needed' column to the
    # corresponding value in 'threebp_gain_needed'
    df.loc[gain_or_loss < 0, 'threebp_gain_needed'] = threebp_gain_needed

    df = df.fillna('')

    return df


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


def save_to_html_and_open(df):
    with open("data.html", "w") as f:
        f.write(df.to_html())
    webbrowser.open('file://' + os.path.realpath("data.html"))


def threebp_main(df):
    df = check_for_buy_conditions(df)
    save_to_html_and_open(df)
    return df
# 