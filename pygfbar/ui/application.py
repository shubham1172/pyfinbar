import tkinter as tk
import threading
import time
from pygfbar.data import SheetReader
from tkhtmlview import HTMLLabel

STOCK_DISPLAY_XPAD = 4
STOCK_DISPLAY_YPAD = 4
STR_FETCHING_DATA = "Fetching the latest data..."


class App(tk.Frame):
    def __init__(self, parent, refresh_rate, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        exitButton = tk.Button(self, bg="red", fg="white", text='X', command=self.exit, anchor='e')
        exitButton.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.stockDisplay = StockDisplayApp(self, refresh_rate)
        self.stockDisplay.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def exit(self):
        self.stockDisplay.stop()
        self.parent.destroy()


class StockDisplayApp(tk.Canvas):
    def __init__(self, parent, refresh_rate, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)

        self.refresh_rate = refresh_rate
        self._is_running = True
        self.reader = SheetReader()

        self.html_label = HTMLLabel(self)
        self.html_label.tag = "html_label"
        self.set_text(STR_FETCHING_DATA)
        self.html_label.pack(fill=tk.BOTH, expand=True)

        bg_thread = threading.Thread(target=self.fetch, daemon=True)
        bg_thread.start()

    def fetch(self):
        while self._is_running:
            self.set_text((" "*4).join([x.to_html()
                                        for x in self.reader.get_data()]))
            time.sleep(self.refresh_rate)

    def stop(self):
        self._is_running = False

    def set_text(self, content):
        self.html_label.set_html(
            """<div style=
                \"background-color:%s;
                  color:%s;
                  font-size: %dpx;
                  text-align:%s;\">%s</div>""" %
            ("black", "white", 10, "left", content))
