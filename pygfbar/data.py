from pygfbar.auth import Credentials
from pygfbar.config import Config
from pygfbar.console import Colors
from googleapiclient.discovery import build


class StockRecord:
    def __init__(self, ticker, prevclose, close):
        super().__init__()
        self.ticker = ticker
        self.prevclose = prevclose
        self.close = close

    def change(self):
        return 100*(self.close - self.prevclose)/self.close

    def __str__(self):
        delta = self.change()
        if delta > 0:
            color = Colors.GREEN
        elif delta < 0:
            color = Colors.RED
        else:
            color = Colors.GRAY
        return "%s %.2f %.2f " % (self.ticker, self.prevclose, self.close) \
            + color + "%.2f%%" % delta + Colors.ENDC


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
            xs.append(StockRecord(row[0], float(row[1]), float(row[2])))

        return xs
