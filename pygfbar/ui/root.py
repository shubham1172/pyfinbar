import tkinter as tk
from pygfbar.ui.application import App

def get_root(ypos, refresh_rate):
    root = tk.Tk()

    # hide the title bar
    root.overrideredirect(True)

    # always on top
    root.wm_attributes('-topmost', True)

    # set geometry
    set_root_dims(root, ypos)

    # add app
    app = App(root, refresh_rate)
    app.pack(fill="both", expand="True")
    return root

def set_root_dims(root, ypos):
    w = root.winfo_screenwidth()
    h = 25
    x = 0
    y = (ypos/100) * root.winfo_screenheight()
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
