import os
import shutil
import tkinter
# paths
origin = # filepath to your save00 repository here. example "C:\\Users\\me\\AppData\\LocalLow\\Nolla_games_noita\\save00"

destination = # filepath to where you want to save your games. example "C:\\Users\\me\\Documents\\FolderInDocuments\\save00"



# the two needed functions, save and load
def save():
    savegame = option_var.get()
    if savegame == optionslist[0]:
        destination = # see destination above but replace save00 with save01
        if os.path.exists(destination):
            shutil.rmtree(destination)
        shutil.copytree(origin, destination)
        status.set("game saved")
    if savegame == optionslist[1]:
        destination = # see destination above but replace save00 with save02
        if os.path.exists(destination):
            shutil.rmtree(destination)
        shutil.copytree(origin, destination)
        status.set("game saved")
    if savegame == optionslist[2]:
        destination = # see destination above but replace save00 with save03
        if os.path.exists(destination):
            shutil.rmtree(destination)
        shutil.copytree(origin, destination)
        status.set("game saved")


def load():
    savegame = option_var.get()
    if savegame == optionslist[0]:
        print(savegame)
        destination = # see destination above but replace save00 with save01
        if os.path.exists(origin):
            shutil.rmtree(origin)
        shutil.copytree(destination, origin)
        status.set("game saved")
    if savegame == optionslist[1]:
        destination = # see destination above but replace save00 with save02
        if os.path.exists(origin):
            shutil.rmtree(origin)
        shutil.copytree(destination, origin)
        status.set("game saved")
    if savegame == optionslist[2]:
        destination = # see destination above but replace save00 with save03
        if os.path.exists(origin):
            shutil.rmtree(origin)
        shutil.copytree(destination, origin)
        status.set("game saved")

#the gui setup
root = tkinter.Tk()
root.title("Noita saver")
root.geometry('250x250')
root.resizable(False, False)

# credits for my enormous effort put into this program
txtlabel = tkinter.Label(text="made by Willie\n"
                      "Don't try to load a save while the game is running, \n"
                      " you will lose the save you're trying to load if you do.",
                 font=('Arial',7))
txtlabel.pack(side=tkinter.BOTTOM)

# buttons frame
buttonframe = tkinter.Frame(root)
buttonframe.place(relx=0.5, rely=0.5,
                  anchor=tkinter.CENTER)
# save button front end
save = tkinter.Button(buttonframe,
              text="save",
              font=('arial', 20),
              command=save)

save.pack()
# option menu for posible saves
optionslist = ('save 1', 'save 2', 'save 3')
option_var = tkinter.StringVar(buttonframe)
option_var.set(optionslist[0])
OM = tkinter.OptionMenu(buttonframe,
                        option_var,
                        *optionslist)

OM.pack()
# load button front end
load = tkinter.Button(buttonframe,
              text="load",
              font=('arial', 20),
              command= load)
load.pack()

# status label
status =tkinter.StringVar()
statuslabel = tkinter.Label(buttonframe,
                    textvariable=status,
                    font=('Arial', 14))
statuslabel.pack()
root.mainloop()

print(os.path.getsize("noitasaver.py"))
