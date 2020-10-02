import json
from pygfbar.common import SingletonMeta


class Config(metaclass=SingletonMeta):
    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)

    def spreadsheetId(self):
        return self.config["SpreadsheetId"]
