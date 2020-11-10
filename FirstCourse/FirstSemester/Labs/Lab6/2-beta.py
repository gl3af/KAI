import threading
import time
from tkinter import *


def heart(event):
    x = -1.0
    step = 0.001
    stop = 1.0
    delay = 0.001
    while x <= stop:
        if x == 0:
            y1 = 1.0
            y2 = -1.0
            c.create_rectangle(170 + x * 100 + 100, 170 - y1 * 100, 170 + x*100 + 100, 170 - y1 * 100, outline='red')
            c.create_rectangle(170 + x * 100 + 100, 170 - y2 * 100, 170 + x*100 + 100, 170 - y2 * 100, outline='red')
        else:
            d = 4 * abs(x) - 4 * (x ** 2 + abs(x) - 1)
            d = round(d, 2)
            if d == 0:
                y1 = abs(x) ** 0.5
                y1 = round(y1, 2)
                c.create_rectangle(170 + x * 100 + 100, 170 - y1 * 100, 170 + x*100 + 100, 170 - y1*100, outline='red')
                time.sleep(delay)
            else:
                y1 = (2 * abs(x) ** 0.5 + d ** 0.5) / 2
                y1 = round(y1, 2)
                y2 = (2 * abs(x) ** 0.5 - d ** 0.5) / 2
                y2 = round(y2, 2)
                c.create_rectangle(170 + x * 100 + 100, 170 - y1 * 100, 170 + x*100 + 100, 170 - y1*100, outline='red')
                c.create_rectangle(170 + x * 100 + 100, 170 - y2 * 100, 170 + x*100 + 100, 170 - y2*100, outline='red')
                time.sleep(delay)
        x += step


root = Tk()
c = Canvas(root, width=540, height=270, bg="white")
c.pack()

rect = c.create_rectangle(0, 150, 0, 150, outline='red')
thread = threading.Thread(target=heart, name="thr", args=[c])
thread.start()

root.mainloop()
