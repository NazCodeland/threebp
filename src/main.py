# from schedule_tasks import schedule_tasks
from data.yahoo_finance import download_from_yahoo
from data.database import upload_to_db, download_from_db
from lib.threebp import threebp_main
from config import symbols, timeframes
from data.google_sheets import upload_to_gsheets  
import os
import pandas as pd
import models
from lib.charts import plot_chart
from data.barchart import extract_industry_equities




# Usage:
if __name__ == '__main__':
    symbols = ['CTS.TO']
    
    def download_from_yahoo_and_upload_to_db():
        for symbol in symbols:
            # returns a DataFrame
            data = download_from_yahoo(symbol, 'mo')
            for timeframe in timeframes:
                upload_to_db(data, symbol, timeframe)
                # save_df(data, symbol, "csv")
    # download_from_yahoo_and_upload_to_db()

    # df = download_from_db()
    # save the DataFrame locally in a file called "TSX"
    # save_df(df, "TSX", "csv")

    # df = pd.read_csv("src/prices/TSX.csv")
    # df = threebp_main(df)

    # Upload the DataFrame to Google Sheets
    # upload_to_gsheets(df)


    # schedule_tasks(symbol, timeframe)


# MVC Model
# def main():
#     # Create the Model
#     model = Model()

#     # Create the View, passing it the Model so it knows what to display
#     view = View(model)

#     # Create the Controller, passing it both the Model and the View
#     controller = Controller(model, view)

#     # Enter the application's main event loop
#     controller.run()

# # Call the main function to start the application
# if __name__ == "__main__":
#     main()