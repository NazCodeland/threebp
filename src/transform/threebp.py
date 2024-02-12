
import pandas as pd
import numpy as np

from transform.transform_functions import save_to_html_and_open


def check_for_buy_conditions(df):
    # -------------------------------------------------------
    # TODO: move this somewhere else
    # turn 'volume' column into dollar denominated values
    df['volume'] = ((df['volume'] * df['close']) / 1000000).round(2)

    # setting up columns for bullish 3bp marks
    # Calculate the conditions for higher high and higher close
    higher_high = df['high'].shift(-1) >= df['high'].shift(-3)
    higher_close = df['close'].shift(-1) >= df['close'].shift(-2)

    # Calculate the condition for not checking (when the high of 2 bars ago is not greater than the high of 4 bars ago)
    dont_check = df['high'].shift(-2) <= df['high'].shift(-4)
    # Calculate the bullish 3 bar play condition
    # This will be True only when higher_high, higher_close, and dont_check are all True
    bullish_3bp = dont_check & higher_high & higher_close


    # setting up columns for bearish 3bp marks
    # lower_low = df['low'].shift(-1) < df['low'].shift(-3)
    # lower_close = df['close'].shift(-1) < df['close'].shift(-2)

    # gain or loss from last bars close
    # gain_or_loss = ((df['close'].shift(-1) - df['close'].shift(-2)) * 100) / df['close'].shift(-2)

    # if not in a bullish 3bp, calculate gain needed from current price to form a bullish 3bp
    threebp_highmark = np.maximum(df['close'].shift(-2), df['high'].shift(-3))
    threebp_gain_needed = -round(((threebp_highmark - df['close'].shift(-1)) * 100) / df['close'].shift(-1), 2)

    df['3bp'] = bullish_3bp
    df['3bpGainNeeded'] = threebp_gain_needed
    df['3bpValue'] = np.where(df['3bp'], 'True', df['3bpGainNeeded'])

    

    # # if not in a bullish 3bp, calculate gain needed from current price to form a bullish 3bp
    # threebp_highmark = np.maximum(df['close'].shift(-1), df['high'].shift(-2))
    # threebp_gain_needed = -((threebp_highmark - df['close']) * 100) / df['close']

    # # For rows where 'gain_or_loss' is greater than or equal to 0, set the 'gain_or_loss'
    # # column to the corresponding value in 'gain_or_loss'
    # df.loc[gain_or_loss >= 0, 'gain_or_loss'] = gain_or_loss
    # # For rows where 'gain_or_loss' is less than 0, set the 'gain_or_loss' column to NaN
    # df.loc[gain_or_loss < 0, 'gain_or_loss'] = float('nan')
    # # For rows where 'gain_or_loss' is greater than or equal to 0, set the 'threebp_gain_needed'
    # # column to NaN
    # df.loc[gain_or_loss >= 0, 'threebp_gain_needed'] = float('nan')
    # # For rows where 'gain_or_loss' is less than 0, set the 'threebp_gain_needed' column to the
    # # corresponding value in 'threebp_gain_needed'
    # df.loc[gain_or_loss < 0, 'threebp_gain_needed'] = threebp_gain_needed

    # df = df.fillna('')
    return df



def threebp_main(df):


    # Group the DataFrame by 'symbol' and 'interval' columns, and apply the 'check_for_buy_conditions' function to each group.
    # The 'observed=True' argument means that only the groups that are observed in the data are considered.
    df = df.groupby(['symbol', 'interval'], group_keys=True).apply(check_for_buy_conditions)

    # Reset the index of the DataFrame. The 'droplevel' function removes the specified levels from the index.
    # Here, it's removing 'symbol' and 'interval' levels from the index.
    df.index = df.index.droplevel(['symbol', 'interval'])

    # Group the DataFrame again by 'symbol' and 'interval' columns, and take the first row from each group.
    # The 'reset_index' function is used to reset the index of the DataFrame after the grouping.
    df = df.groupby(['symbol', 'interval'], group_keys=True).first().reset_index()

    # Modify the 'symbol' column to include the Yahoo Finance URL for each symbol

    # df['symbol'] = df['symbol'].apply(lambda x: f'<a href="https://finance.yahoo.com/chart/{x}" target="_blank">{x}</a>')

    # Pivot the DataFrame on '3bp' column
    df_pivot = df.pivot(index='symbol', columns='interval', values='3bpValue')

    # Reset the index
    df_pivot.reset_index(inplace=True)

    # Fill NaN values with False (or any other value you prefer)
    # df_pivot.fillna('', inplace=True)

    # Remove the column name for multi-index columns
    df_pivot.columns.name = None
    return df_pivot



