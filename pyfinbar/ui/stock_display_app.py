import tkinter as tk
import threading
import time
from pyfinbar.config import Config
from pyfinbar.client import MoneyControlStock
from pyfinbar.ui.stock_record_frame import StockRecordFrame
from pyfinbar.stock_record import StockRecord

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

        self.parent.bind("<Button-1>", self.stop)

        bg_thread = threading.Thread(target=self.fetch, daemon=True)
        bg_thread.start()

    def populate(self, records):
        for i, record in enumerate(records[:Config().maxVisibleStocks()]):
            frame = StockRecordFrame(self.parent, record, 0, i)

    def fetch(self):
        epoch = 0
        while self._is_running:
            source_data = MoneyControlStock.fetch_values()
            if (len(source_data) <= Config().maxVisibleStocks()):
                # don't do anything if we can fit all the stocks
                self.populate(source_data)
            else:
                # left rotate based on the epoch
                self.populate(left_rotate_array(source_data, epoch))
                epoch = (epoch + 1) % len(source_data)
            time.sleep(self.refresh_rate)

    def stop(self, event):
        self._is_running = False
        self.parent.destroy()
