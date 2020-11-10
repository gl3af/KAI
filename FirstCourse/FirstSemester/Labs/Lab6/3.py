import threading
from tkinter import *
import time


def action(event):
    while True:
        c.itemconfig(circle_top, fill="red")
        time.sleep(7)
        c.itemconfig(circle_mid, fill="yellow")
        time.sleep(2)
        c.itemconfig(circle_top, fill="grey")
        c.itemconfig(circle_mid, fill="grey")
        c.itemconfig(circle_bot, fill="green")
        time.sleep(5)
        c.itemconfig(circle_bot, fill="grey")
        c.itemconfig(circle_mid, fill="yellow")
        time.sleep(2)
        c.itemconfig(circle_mid, fill="grey")


root = Tk()
root.title("Traffic Light")
c = Canvas(root, width=200, height=600, bg="black")
c.pack()
circle_top = c.create_oval(0, 0, 200, 200, fill="grey")
circle_mid = c.create_oval(0, 200, 200, 400, fill="grey")
circle_bot = c.create_oval(0, 400, 200, 600, fill="grey")
thread = threading.Thread(target=action, name="thr", args=[c])
thread.start()
root.mainloop()
