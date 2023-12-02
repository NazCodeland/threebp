from sqlalchemy import create_engine
import pandas as pd
from config import symbols, dataframe_timeframes, sectors

engine = create_engine("postgresql://investingclarity:nd8FR6gDZvsN@ep-twilight-lake-06412150.us-east-1.aws.neon.tech/neondb?sslmode=require")

def download_from_db(tablename, timeframe=None):
    tablename = f"{tablename}_{timeframe}" if timeframe else tablename
    query = f"SELECT * FROM {tablename}"
    # pd.read_sql_query() returns a DataFrame
    df = pd.read_sql_query(query, engine)
    return df

def upload_to_db(df, tablename, timeframe=None):
    print('uploading')
    # Define the table name
    tablename = f"{tablename}_{timeframe}" if timeframe else tablename
    # Upload the DataFrame to the database
    df.to_sql(tablename, engine, if_exists='replace', index=False)

# another function that scraps the closing day and uploads
# that data to the database. This would eliminate the need to 
# download daily data for all the symbols at the end of the day in
# the scheduler
