import tkinter as tk
from pyfinbar.ui.stock_display_app import StockDisplayApp


def get_root(ypos, refresh_rate, max_visible_stocks):
    root = tk.Tk()
    root.configure(bg="black")

    # hide the title bar
    root.overrideredirect(True)

    # always on top
    root.wm_attributes('-topmost', True)

    # set geometry
    set_root_dims(root, ypos)

    # setup grid
    root.grid_rowconfigure(0, weight=1)

    # add app
    app = StockDisplayApp(root, refresh_rate, max_visible_stocks)
    app.grid(row=0, column=0)

    return root


def set_root_dims(root, ypos):
    w = root.winfo_screenwidth()
    h = 25
    x = 0
    y = (ypos/100) * root.winfo_screenheight()
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
