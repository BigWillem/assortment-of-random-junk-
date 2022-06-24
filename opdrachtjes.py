import tkinter
from tkinter import *
import os
import shutil
from downloader import Downloadimage

def mongen():


    path = "C:\\Users\\tijnf\\Pictures\\zieke_aap.gif"



    def click1():

        Downloadimage()



    def click2():

        try:

            shutil.move('C:\\Users\\tijnf\\Desktop\\coole_aap.png','C:\\Users\\tijnf\\Documents\\kopie van map\\coole_aap.png')

            print("File moved")

        except FileNotFoundError:

            print("File not found dummy boy")



    def click3():

        try:

            os.remove('C:\\Users\\tijnf\\Documents\\kopie van map\\coole_aap.png')

            print("File removed")

        except FileNotFoundError:

            print("File not found dumby boy")



    window = Tk()

    button1 = Button(window,

                    text= "click this button lol",

                    command=click1,

                    font=("arial black", 10),

                    fg=("black"),

                    bg=('white'),

                    activebackground=('white'),

                    activeforeground=('black'),

                    state=ACTIVE,

                    compound='left')



    button2 = Button(window,text= "click this button afterwards lol",

                    command=click2,

                    font=("arial black", 10),

                    fg=("black"),

                    bg=('white'),

                    activebackground=('white'),

                    activeforeground=('black'),

                    state=ACTIVE,

                    compound='center')



    button3 = Button(window,text= "click this button last lol",

                    command=click3,

                    font=("arial black", 10),

                    fg=("black"),

                    bg=('white'),

                    activebackground=('white'),

                    activeforeground=('black'),

                    state=ACTIVE,

                    compound='right')





    bg = PhotoImage(file= path)

    canvas = Canvas(

        window,



    )

    canvas.pack(fill='both', expand= False)



    canvas.create_image(

        0,

        0,

        image= bg,

        anchor= 'nw'

    )



    window.title("Monkey mover")

    button1.pack()

    button2.pack()

    button3.pack()

    window.mainloop()

mongen()
