import tkinter as tk
import threading
import time
from pygfbar.data import SheetReader


class App(tk.Frame):
    def __init__(self, parent, refresh_rate, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        exitButton = tk.Button(self, bg="red", fg="white",
                               text='X', command=self.exit, anchor='e')
        exitButton.pack(side=tk.RIGHT)

        self.stockDisplay = StockDisplayApp(self, refresh_rate)
        self.stockDisplay.pack(fill="both")

    def exit(self):
        self.stockDisplay.stop()
        self.parent.destroy()


class StockDisplayApp(tk.Canvas):
    def __init__(self, parent, refresh_rate, *args, **kwargs):
        tk.Canvas.__init__(self, parent, bg="black", *args, **kwargs)

        self.refresh_rate = refresh_rate

        self.text_id = self.create_text(
            4, 2, fill="white", text="Fetching the latest data...", anchor='nw')

        self.reader = SheetReader()

        self._is_running = True
        bg_thread = threading.Thread(target=self.update, daemon=True)
        bg_thread.start()

    def update(self):
        while self._is_running:
            text = "\t".join([x.to_string() for x in self.reader.get_data()])
            self.itemconfig(self.text_id, text=text)
            time.sleep(self.refresh_rate)

    def stop(self):
        self._is_running = False
