import json
from typing import List
from pyfinbar.common import SingletonMeta

DEFAULT_MAX_VISIBLE_STOCKS = 4


class Config(metaclass=SingletonMeta):
    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)

    def maxVisibleStocks(self) -> int:
        value = self.config.get("MaxVisibleStocks", None)
        return value if value else DEFAULT_MAX_VISIBLE_STOCKS

    def getStocks(self) -> List[List]:
        stocks = []
        value = self.config.get("Stocks", [])
        for v in value:
            try:
                ticker = v["Ticker"]
                symbol = v["Symbol"]
                type_ = v.get("Type", None)
                stocks.append([ticker, symbol, type_])

            except KeyError as ke:
                raise AttributeError(
                    "Invalid config.json. " + str(ke))
        return stocks
