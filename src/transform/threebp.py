
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

    # Calculate the bnt (when the high of 2 bars ago is not greater than the high of 4 bars ago)
    bnt = (df['high'].shift(-2) <= df['high'].shift(-4)) & higher_high & higher_close

    # Calculate the bullish 3 bar play condition
    # This will be True only when higher_high, higher_close are True
    bullish_3bp = higher_high & higher_close


    # setting up columns for bearish 3bp marks
    # lower_low = df['low'].shift(-1) < df['low'].shift(-3)
    # lower_close = df['close'].shift(-1) < df['close'].shift(-2)

    # gain or loss from last bars close
    # gain_or_loss = ((df['close'].shift(-1) - df['close'].shift(-2)) * 100) / df['close'].shift(-2)

    # if not in a bullish 3bp, calculate gain needed from current price to form a bullish 3bp
    threebp_highmark = np.maximum(df['close'].shift(-2), df['high'].shift(-3))
    threebp_gain_needed = -round(((threebp_highmark - df['close'].shift(-1)) * 100) / df['close'].shift(-1), 2)


    df['bnt'] = np.where(bnt, df['interval'], False)
    df['3bpValue'] = np.where(bullish_3bp, 'True', threebp_gain_needed)

    

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
    df = df.groupby(['symbol', 'interval'], group_keys=True).apply(check_for_buy_conditions)

    # After the groupby operation, 'symbol' and 'interval' become part of the index. 
    # This line removes 'symbol' and 'interval' from the index, making them regular columns again.
    # This is necessary for the pivot operation later on, which requires 'symbol' and 'interval' to be regular columns.
    df.index = df.index.droplevel(['symbol', 'interval'])

    # This line groups the DataFrame again by 'symbol' and 'interval' columns and takes the first row & resets the index
    df = df.groupby(['symbol', 'interval'], group_keys=True).first().reset_index()
    print(df)
    # This line is also commented out, but if it were active, it would modify the 'symbol' column to include the Yahoo Finance URL for each symbol.
    # This could be useful if you want to provide a direct link to the Yahoo Finance page for each symbol in your final output.
    # df['symbol'] = df['symbol'].apply(lambda x: f'<a href="https://finance.yahoo.com/chart/{x}" target="_blank">{x}</a>')

    # Pivot the DataFrame on '3bp' column. This reshapes the data, with the 'symbol' column as the index, 
    # the 'interval' column values as the new columns, and the '3bpValue' column values as the new values.
    df_pivot = df.pivot(index='symbol', columns='interval', values='3bpValue')

    # Reset the index of the pivoted DataFrame. This makes 'symbol' a regular column again, and introduces a default integer index.
    df_pivot.reset_index(inplace=True)

    # This line creates a new DataFrame for the 'bnt' column. 
    # Checks the `bnt` column value and if it's not False, it takes the corresponding value (which is an interval), 
    # and aggregates those interval values by symbol.    
    df_bnt = df.groupby('symbol')['bnt'].apply(lambda x: ', '.join([x[i] for i in x.index if x[i] != False]))

    # Merge the 'bnt' DataFrame with the pivoted DataFrame
    df_final = pd.merge(df_bnt, df_pivot, on='symbol', how='left')


    # This line is commented out, but if it were active, it would fill NaN values with an empty string (or any other value you prefer).
    # This could be useful if you want to replace missing values with a specific value.
    # df_pivot.fillna('', inplace=True)

    # Remove the column name for multi-index columns. This is done for cleaner output, as the column name is not necessary in this case.
    df_final.columns.name = None

    # Return the final pivoted DataFrame
    return df_final




