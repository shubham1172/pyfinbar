from pygfbar.console import Colors


class StockRecord:
    '''StockRecord represents the state of a stock.
    Ticker is the stock symbol.
    Prevclose is the last day's closing price.
    Close is today's closing price.

    usage:

    record = StockRecord("YESBANK", 12, 14.5)
    '''

    def __init__(self, ticker, prevclose, close):
        super().__init__()
        self.ticker = ticker
        self.prevclose = prevclose
        self.close = close

    def change(self):
        return 100*(self.close - self.prevclose)/self.close

    def to_string(self, colored=False):
        delta = self.change()
        s = "%s %.2f " % (self.ticker, self.close)
        suff = "%+.2f%%" % delta

        if not colored:
            return s + suff

        if delta > 0:
            color = Colors.GREEN
        elif delta < 0:
            color = Colors.RED
        else:
            color = Colors.GRAY
        return s + color + suff + Colors.ENDC

    def to_object(self):
        return \
            {
                "TICKER": self.ticker,
                "CLOSE": "%.2f" % self.close,
                "CHANGE": "%+.2f%%" % self.change()
            }

    def __str__(self):
        return self.to_string()
