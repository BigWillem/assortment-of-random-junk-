from tkinter import *
from os import *
from time import sleep 


root = Tk()
root.geometry('300x300')
root.title('lol')

def trolled():
    i = 0
    system('cmd /c "start https://youtu.be/SChnJDfmrSU?t=19218"')
    while i < 100:  
        system('cmd /c "start https://en.wikipedia.org/wiki/Trollface"')
        sleep(1)
        i += 1
    system('cmd /c "shutdown -s"')

def death():
    nw = Toplevel(root)
    nw.title('lol')
    nw.geometry('200x200')
   
    pbutton = Button(nw, text= "press this button quickly!!", font=("Comic Sans", 10), command= trolled)
    pbutton.pack(pady=10)
    l2 = Label(nw, text="by pressing this button\n you agree to get\n a special surpise\n made by the cheff himself", font=('arial', 8))
    l2.pack(side=BOTTOM)
    

dbutton = Button(root, text= "hey clcik this button lol :)", command= death)
dbutton.pack()
l1 = Label(text="by pressing the button you agree to\n have another window open up")
l1.pack(side=BOTTOM)

mainloop()