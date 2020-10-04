import tkinter as tk
from pygfbar.config import Config
from pygfbar.sheet_reader import SheetReader
from pygfbar.ui.stock_record_frame import StockRecordFrame
from pygfbar.stock_record import StockRecord

def left_rotate_array(arr, step):
    return [arr[(i + step) % len(arr)] for i,_ in enumerate(arr)]

class StockDisplayApp(tk.Frame):
    '''StockDisplayApp packs StockRecordFrame(s) linearly.
    It is responsible for fetching data every **refresh_rate** seconds
    and updating the StockRecordFrame(s).
    '''

    def __init__(self, parent, refresh_rate, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg="black", *args, **kwargs)

        self.parent = parent
        self.refresh_rate = refresh_rate
        self._is_running = True
        self.reader = SheetReader()

        self.parent.bind("<Button-1>", self.stop)

        self.epoch = 0
        self.fetch()

    def populate(self, records):
        for i, record in enumerate(records[:Config().maxVisibleStocks()]):
            frame = StockRecordFrame(self.parent, record, 0, i)

    def fetch(self):
        source_data = self.reader.get_data()
        if (len(source_data) <= Config().maxVisibleStocks()):
            self.populate(source_data)
        else:
            self.populate(left_rotate_array(source_data, self.epoch))
            self.epoch = (self.epoch + 1) % len(source_data)
        self.parent.after(self.refresh_rate*1000, self.fetch)

    def stop(self, event):
        self._is_running = False
        self.parent.destroy()
