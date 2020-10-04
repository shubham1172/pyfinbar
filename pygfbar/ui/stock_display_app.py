import tkinter as tk
import threading
import time
from pygfbar.config import Config
from pygfbar.sheet_reader import SheetReader
from pygfbar.ui.stock_record_frame import StockRecordFrame
from pygfbar.stock_record import StockRecord


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

        bg_thread = threading.Thread(target=self.fetch, daemon=True)
        bg_thread.start()

    def populate(self, records):
        for i, record in enumerate(records[:Config().maxVisibleStocks()]):
            frame = StockRecordFrame(self.parent, record, 0, i)

    def fetch(self):
        while self._is_running:
            self.populate(self.reader.get_data())
            time.sleep(self.refresh_rate)

    def stop(self, event):
        self._is_running = False
        self.parent.destroy()
