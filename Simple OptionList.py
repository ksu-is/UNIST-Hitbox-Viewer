from tkinter import *

characters = ["Hilda", "Hyde", "Chaos"]

master = Tk()

master.title("UNIST Hitbox Viewer")

master.minsize(500,500)

variable = StringVar(master)
variable.set(characters[0])

w = OptionMenu(*(master, variable) + tuple(characters))
w.pack(side=TOP, anchor=W) 

mainloop()
