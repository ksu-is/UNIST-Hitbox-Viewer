from tkinter import *

#sets list of characters
characters = ["Hilda", "Hyde", "Chaos"]

#creates list of moves
moves = ["2b", "5b", "2c"]

master = Tk()

#sets title of the program
master.title("UNIST Hitbox Viewer")

#sets the minimum size of the window to 500x500
master.minsize(500,500)

#creates stringvar, sets the default value to the first item in the list
characterMenu = StringVar(master)
characterMenu.set(characters[0])

#creates stringvar, sets default value to first item in list
moveMenu = StringVar(master)
moveMenu.set(moves[0])

#creates character dropdown menu, anchors it to the top left
w = OptionMenu(*(master, characterMenu) + tuple(characters))
w.pack(side=LEFT, anchor=N) 

#creates move dropdown menu, anchors it to the right of the characters
x = OptionMenu(*(master, moveMenu) + tuple(moves))
x.pack(side=TOP, anchor=W)

#creates two variables to store the selections from the dropdown menus
characterSelection = ''
moveSelection = ''

#creates button
class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, config)
        self.pack(side=RIGHT, anchor=N)
        self.config(command=self.callback)
    def callback(self):
        self.quit()
        
#gets the selection from the menus
class MyButton(HelloButton):
    def callback(self):
        characterSelection = characterMenu.get()
        moveSelection = moveMenu.get()
        #prints the selections from the dropdown menu for reference
        print( characterMenu.get())
        print( moveMenu.get())

if __name__ == "__main__":
    MyButton(None, text="Load").mainloop()

#if characterSelection == "Hilda":
#    if moveSelection == "5b":

#starts GUI
mainloop()
