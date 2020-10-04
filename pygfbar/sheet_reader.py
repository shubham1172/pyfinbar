from pygfbar.auth import Credentials
from pygfbar.config import Config
from pygfbar.stock_record import StockRecord
from googleapiclient.discovery import build


class SheetReader:
    def __init__(self):
        self.config = Config()
        self.creds = Credentials()
        self.service = build('sheets', 'v4', credentials=self.creds.get())
        self.sheet = self.service.spreadsheets()

    def get_data(self):
        xs = []

        result = self.sheet.values().get(
            spreadsheetId=self.config.spreadsheetId(), range='A:C').execute()
        values = result.get('values', [])

        for row in values:
            # prevents stray data
            if len(row) == 3:
                xs.append(StockRecord(row[0], float(row[2]), float(row[1])))

        return xs
