import json
from typing import List
from pyfinbar.common import SingletonMeta


class Config(metaclass=SingletonMeta):
    FILENAME = "stocks.json"

    def __init__(self):
        with open(Config.FILENAME) as f:
            self.stocks = json.load(f)

    def getStocks(self) -> List[List]:
        stocks = []
        value = self.stocks
        for v in value:
            try:
                ticker = v["Ticker"]
                symbol = v["Symbol"]
                type_ = v.get("Type", None)
                stocks.append([ticker, symbol, type_])

            except KeyError as ke:
                raise AttributeError(
                    f"Invalid {Config.FILENAME}. Missing {str(ke)}.")
        return stocks
