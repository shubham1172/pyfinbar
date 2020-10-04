import tkinter as tk
from pygfbar.stock_record import StockRecord


class _StockRecordFrameLabel(tk.Label):
    def __init__(self, text, fg="white", bg="black", *args, **kwargs):
        super().__init__(text=text, foreground=fg, background=bg, *args, **kwargs)


class StockRecordFrame(tk.Frame):
    '''StockRecordFrame displays a stock record
    
    usage:
    
    record = StockRecord("SENSEX", 100, 120)
    frame = StockRecordFrame(record, row, column)

    It is made up of labels including one label for padding
    '''
    def __init__(self, record: StockRecord, r, c, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.bold_font = "Helvetica 12 bold"

        # TICKER
        label_ticker = _StockRecordFrameLabel(
            record.ticker, font=self.bold_font)
        label_ticker.grid(row=r, column=c*4, sticky="nsew")

        # CLOSE VALUE
        label_close = _StockRecordFrameLabel("%.2f" % record.close)
        label_close.grid(row=r, column=c*4+1, sticky="nsew")

        # CHANGE PERCENTAGE
        label_change_color = "green" if record.change() > 0 else (
            "red" if record.change() < 0 else "gray")
        label_change = _StockRecordFrameLabel(
            "%+.2f%%" % record.change(), fg=label_change_color)
        label_change.grid(row=r, column=c*4+2, sticky="nsew")

        # PADDING
        label_empty = _StockRecordFrameLabel(" "*2)
        label_empty.grid(row=r, column=c*4+3, sticky="nsew")
