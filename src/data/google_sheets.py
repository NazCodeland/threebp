import gspread
from gspread_dataframe import set_with_dataframe
from config import email

def upload_to_gsheets(df):
    # Use your own credentials.json
    gc = gspread.service_account(filename='./client_secret.json')

    # Try to open the Google Spreadsheet
    try:
        sh = gc.open("TSX")
    except gspread.SpreadsheetNotFound:
        # If not found, create a new one
        sh = gc.create("TSX")

    # Share the document with your personal Google account
    # sh.share(email, perm_type='user', role='writer')
    
    print("New spreadsheet created. URL:", sh.url)
    # Select Spreadsheet's sheet
    worksheet = sh.sheet1

    # Upload the DataFrame to Google Sheets
    set_with_dataframe(worksheet, df)
