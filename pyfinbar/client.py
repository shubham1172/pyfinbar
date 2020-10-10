import requests
from typing import List
from pyfinbar.config import Config
from pyfinbar.stock_record import StockRecord


class MoneyControlStock:
    BASE_API_TEMPLATE = "https://priceapi.moneycontrol.com/pricefeed/{0}/{1}"

    DEFAULT_TYPE_ = "NSE"

    EXCHANGE_MAP = {
        "NSE": "nse/equitycash",
        "BSE": "bse/equitycash",
        "INDEX": "notapplicable/inidicesindia"
    }

    def __init__(self, ticker, symbol, type_):
        self.ticker = ticker
        self.symbol = symbol
        # validate type_
        type_ = type_ if type_ else MoneyControlStock.DEFAULT_TYPE_
        if type_ not in MoneyControlStock.EXCHANGE_MAP.keys():
            raise KeyError(
                f'Invalid type {type_}. Allowed types {", ".join(MoneyControlStock.EXCHANGE_MAP.keys())}')
        self.type_ = type_
        self.url = self.getUrl()

    def fetch_value(self) -> StockRecord:
        r = requests.get(self.url)
        if r.status_code == 200:
            s = r.json().get("data", None)
            return StockRecord(self.ticker, float(s["priceprevclose"]), float(s["pricecurrent"])) if s else None
        return None

    @staticmethod
    def fetch_values() -> List[StockRecord]:
        return [MoneyControlStock(*s).fetch_value() for s in Config().getStocks()]

    def getUrl(self) -> str:
        # INDICES are represented as in;NSX, in;SEN, etc.
        symbol = f"in%3B{self.symbol}" if self.type_ == "INDEX" else self.symbol

        return MoneyControlStock.BASE_API_TEMPLATE.format(
            MoneyControlStock.EXCHANGE_MAP[self.type_], symbol)
