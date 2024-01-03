from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from config import email
import pandas as pd

def upload_to_gsheets(df):
    # Use your own credentials.json
    creds = Credentials.from_service_account_file('src/load/client_secret.json')
    service = build('sheets', 'v4', credentials=creds)

    # Create a new Google Spreadsheet
    spreadsheet = {
        'properties': {
            'title': "threebp"
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                        fields='spreadsheetId').execute()

    print('New spreadsheet created. ID:', spreadsheet.get('spreadsheetId'))

    # Upload the DataFrame to Google Sheets
    data = []
    data.append(df.columns.tolist())
    data.extend(df.values.tolist())
    body = {
        'values': data
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet.get('spreadsheetId'), range="Sheet1!A1",
        valueInputOption='RAW', body=body).execute()

    # Share the document with your personal Google account
    drive_service = build('drive', 'v3', credentials=creds)
    file_id = spreadsheet.get('spreadsheetId')
    user_permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': email
    }
    command = drive_service.permissions().create(
        fileId=file_id,
        body=user_permission,
        fields='id',
    )
    command.execute()




def call_apps_script():
    creds = Credentials.from_service_account_file('src/load/google_app_sheet.json')
    service = build('script', 'v1', credentials=creds)

    request = {
        'function': 'createFilter'
    }

    response = service.scripts().run(
        scriptId='1EQPoCBXQkGicGe8qs-QMKUINOXLgkbAVTl-F-UUmaRrUYqTUj3W1x6aO',  # Replace with your script's Project ID
        body=request
    ).execute()

    print('Response from Google Apps Script:', response)
