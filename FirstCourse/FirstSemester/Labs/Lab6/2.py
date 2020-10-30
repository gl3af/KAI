import threading
import time
from tkinter import *
t = 400


def motion(event):
    while True:
        s = c.coords(rect)
        while s[2] < t:
            c.move(rect, 2, 0)
            s = c.coords(rect)
            time.sleep(0.1)
        while s[3] < t:
            c.move(rect, 0, 2)
            s = c.coords(rect)
            time.sleep(0.1)
        while s[0] > 0:
            c.move(rect, -2, 0)
            s = c.coords(rect)
            time.sleep(0.1)
        while s[1] > 0:
            c.move(rect, 0, -2)
            s = c.coords(rect)
            time.sleep(0.1)


root = Tk()
c = Canvas(root, width=t, height=t, bg="grey")
c.pack()

rect = c.create_rectangle(0, 0, 50, 50, fill='white')

thread = threading.Thread(target=motion, name="thr", args=[c])
thread.start()

root.mainloop()
