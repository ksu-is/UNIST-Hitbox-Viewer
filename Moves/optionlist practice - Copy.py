#imports tkinter and PIL
from tkinter import *
from PIL import ImageTk, Image
import os

#intializes tkinter
root = Tk()

this_folder = os.path.dirname(os.path.abspath(__file__))

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

#load image function that will load the first image
def loadImage(character, move):
    
    #will make the file the correct picture for the options the user has chosen.
    if str(character) == "Hilda":
        if str(move) == "5b":
            my_file = os.path.join(this_folder, 'Hilda-5b.png')

        if str(move) == "2b":
            my_file = os.path.join(this_folder, 'Hilda-2b.png')

        if str(move) == "2c":
            my_file = os.path.join(this_folder, 'Hilda-2c.png')
    
    if str(character) == "Hyde":
        if str(move) == "5b":
            my_file = os.path.join(this_folder, 'Hyde-5b.png')

        if str(move) == "2b":
            my_file = os.path.join(this_folder, 'Hyde-2b.png')

        if str(move) == "2c":
            my_file = os.path.join(this_folder, 'Hyde-2c.png')
    
    if str(character) == "Chaos":
        if str(move) == "5b":
            my_file = os.path.join(this_folder, 'Chaos-5b.png')

        if str(move) == "2b":
            my_file = os.path.join(this_folder, 'Chaos-2b.png')

        if str(move) == "2c":
            my_file = os.path.join(this_folder, 'Chaos-2c.png')

    #opens the image in an image object, setting the path of the file to a variable
    img = Image.open(my_file)
    filename = ImageTk.PhotoImage(img)

    #creates a global canvas variable that is set to the size of the image, setting the image on the canvas as the image previously loaded
    global canvas
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

        #destroys the previous image so that the new one will display properly.
        canvas.destroy()

        #prints the selections from the dropdown menu for reference
        #print(characterMenu.get())
        #print(moveMenu.get())
        
        #calls loadImage to load the proper image if that particular image is called for.
        
        loadImage(characterSelection, moveSelection)


if __name__ == "__main__":
    MyButton(None, text="Load").mainloop()


#starts GUI
root.mainloop()
