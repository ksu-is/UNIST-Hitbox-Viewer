from tkinter import *
from PIL import ImageTk, Image

root = Tk()

frame = Frame(root)
prompt = StringVar()

#sets list of characters
characters = ["Hilda", "Hyde", "Chaos"]

#creates list of moves
moves = ["2b", "5b", "2c"]

canvas = Canvas(root, height = 1, width = 1)
#sets title of the program
root.title("UNIST Hitbox Viewer")

#sets the minimum size of the window to 500x500
root.minsize(500,500)

#creates stringvar, sets the default value to the first item in the list
characterMenu = StringVar(root)
characterMenu.set(characters[0])

#creates stringvar, sets default value to first item in list
moveMenu = StringVar(root)
moveMenu.set(moves[0])

#creates character dropdown menu, anchors it to the top left
w = OptionMenu(*(root, characterMenu) + tuple(characters))
w.pack(side=LEFT, anchor=NW) 

#creates move dropdown menu, anchors it to the right of the characters
x = OptionMenu(*(root, moveMenu) + tuple(moves))
x.pack(side=TOP, anchor=NW)

#creates two variables to store the selections from the dropdown menus
characterSelection = ''
moveSelection = ''

#creates button
class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, config)
        self.pack(anchor=SE)
        self.config(command=self.callback)
    def callback(self):
        self.quit()
       
#gets the selection from the menus
class MyButton(HelloButton):
    def callback(self):
        characterSelection = characterMenu.get()
        moveSelection = moveMenu.get()
        #prints the selections from the dropdown menu for reference
        print(characterMenu.get())
        print(moveMenu.get())
        if characterSelection == "Hilda":
            loadImage()


#img = ImageTk.PhotoImage(Image.open('C:/Users/tcarver5/Desktop/code/Hilda-5b.png'))
#with Image.open('C:/Users/tcarver5/Desktop/code/Hilda-5b.png') as image_size:
    #width, height = image_size.size
def loadImage():
    img = Image.open('C:/Users/tcarver5/Desktop/code/Hilda-5b.png')
    filename = ImageTk.PhotoImage(img)

    canvas = Canvas(root, height = img.size[0], width = img.size[0])
    canvas.image = filename
    canvas.create_image(150,150, image=filename)
    canvas.pack()
#canvas.create_image(150, 150, anchor = CENTER, image=img)

if __name__ == "__main__":
    MyButton(None, text="Load").mainloop()


#starts GUI
root.mainloop()
