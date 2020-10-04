import json
from pygfbar.common import SingletonMeta

DEFAULT_MAX_VISIBLE_STOCKS = 8

class Config(metaclass=SingletonMeta):
    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)

    def spreadsheetId(self):
        return self.config["SpreadsheetId"]

    def maxVisibleStocks(self):
        value = self.config.get("MaxVisibleStocks", None)
        return value if value else DEFAULT_MAX_VISIBLE_STOCKS
