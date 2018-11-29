#imports tkinter and PIL
from tkinter import *
from PIL import ImageTk, Image

#intializes tkinter
root = Tk()

#intializes a frame to connect the later canvas to
frame = Frame(root)
prompt = StringVar()

#sets list of characters
characters = ["Hilda", "Hyde", "Chaos"]

#creates list of moves
moves = ["2b", "5b", "2c"]

#creates an initial canvas to later modify
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

#creates a load button
class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, config)
        self.pack(anchor=SE)
        self.config(command=self.callback)
    def callback(self):
        self.quit()

#load image class that will load the first image
def loadImage():
    
    #opens the image in an image object, setting the path of the file to a variable
    img = Image.open('Hilda-5b.png')
    filename = ImageTk.PhotoImage(img)

    #creates a canvas that is the size of the image, setting the image on the canvas as the image previously loaded
    canvas = Canvas(root, height = img.size[0], width = img.size[0])
    canvas.image = filename
    
    #creates the image, anchoring and packing it to view
    canvas.create_image(0,0, anchor = NW, image=filename)
    canvas.pack()

#allows the button to perform functions
class MyButton(HelloButton):
    def callback(self):
        
        #gets the current selection from the dropdown menues
        characterSelection = characterMenu.get()
        moveSelection = moveMenu.get()
        
        #prints the selections from the dropdown menu for reference
        print(characterMenu.get())
        print(moveMenu.get())
        
        #calls loadImage to load the proper image if that particular image is called for.
        if characterSelection == "Hilda":
            if moveSelection == "5b":
                loadImage()


if __name__ == "__main__":
    MyButton(None, text="Load").mainloop()


#starts GUI
root.mainloop()
