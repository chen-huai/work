from tkinter import *
import time
 
def onGo():        
        for i in range(50):
                t.insert(END,'a_'+str(i))
                time.sleep(1)
                 
root = Tk()
t = Text(root)
t.pack()
goBtn = Button(text = "Go!",command = onGo)
goBtn.pack()
root.mainloop()