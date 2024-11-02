from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1FG7goSocxqTHmfDneX1F8d5pc0iGszveIpvS5-SlAhA'
SAMPLE_RANGE_NAME = 'wine!A2:AH'


indexData = []

profileEmail = []

columnCount = 0

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        indexData.clear()

        if not values:
            print('No data found.')
            
        # print('Property Address, City:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            if len(row) >= 1:
                indexData.append('%s' % (row[0]))

    except HttpError as err:
        print(err)


def getColumnCount():
    columnCount = len(indexData)
    return columnCount

def insert_data(data_range,
                index_value, name_value, description_value, volume_value, abv_value, location_value, country_value, producer_value, release_date_value, vintage_value, best_seller_value, style_value, price_value, sugar_content_value,
                flavours_value, sweetness_value, body_value, flavour_intensity_value, tannins_value, acidity_value, total_alcohol_ml_value, varietal_value, value_value, type_value, class_value, subtype_value,
                rating_value, rating_norm_value, value_norm_value, score_norm_value, score_value, images_value, food_parings_value, similar_wines_value):
                
    data = [
        [index_value, name_value, description_value, volume_value, abv_value, location_value, country_value, producer_value, release_date_value, vintage_value, best_seller_value, style_value, price_value, sugar_content_value,
        flavours_value, sweetness_value, body_value, flavour_intensity_value, tannins_value, acidity_value, total_alcohol_ml_value, varietal_value, value_value, type_value, class_value, subtype_value,
        rating_value, rating_norm_value, value_norm_value, score_norm_value, score_value, images_value, food_parings_value, similar_wines_value]
    ]
    data_body = {
        'values': data
    }
    
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Finally, call the API to write the data to the spreadsheet
        result1 = service.spreadsheets().values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=data_range,
                valueInputOption='USER_ENTERED',
                body=data_body
            ).execute()

        print('{0} data updated.'.format(result1.get('updatedCells')))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()