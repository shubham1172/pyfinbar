import tkinter as tk
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

        self.populate([
            StockRecord("MSFT", 90, 100),
            StockRecord("NIFTY", 1000, 1002),
            StockRecord("SENSEX", 1000, 900)])

        #     bg_thread = threading.Thread(target=self.fetch, daemon=True)
        #     bg_thread.start()

    def populate(self, records):
        for i, record in enumerate(records):
            frame = StockRecordFrame(record, 0, i)

    # def fetch(self):
    #     while self._is_running:
    #         self.set_text((" "*4).join([x.to_html()
    #                                     for x in self.reader.get_data()]))
    #         time.sleep(self.refresh_rate)

    def stop(self, event):
        self._is_running = False
        self.parent.destroy()
