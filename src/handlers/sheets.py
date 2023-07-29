from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def append_values(spreadsheet_id, range_name, value_input_option, _values):

    creds, _ = google.auth.default()

    try:
        service = build('sheets', 'v4', credentials=creds)

        body = {
            'values': _values
        }
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        return result

    except HttpError as error:
        return error
