from pygfbar.data import SheetReader
import time

if __name__ == "__main__":
    s = SheetReader()
    while True:
        for x in s.get_data():
            print(x)