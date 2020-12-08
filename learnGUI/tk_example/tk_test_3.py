from tkinter import *
import time

root = Tk()
t = Text(root)
t.pack()
root.update()
it = iter(range(10))

while True:
    t.insert('end',str(next(it)))
    print(next(it))
    root.update()
    time.sleep(1)
root.mainloop()