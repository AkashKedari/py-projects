# Import the modules

import tkinter
from PIL import Image, ImageTk
import random

# Build main window for the application 

root = tkinter.Tk()
root.geometry("400x400")
# Set application title 
root.title("Roll The Dice")

# Adding labels into frame
BlankLine = tkinter.Label(root,text="")
BlankLine.pack()

# Adding label w/custom format/font

HeadingLabel = tkinter.Label(root, text="Akash's Dice Roller",
    fg = "light green",
        font = "Helevtica 16 bold italic")
HeadingLabel.pack()

# Images 
dice = ('Alea_1.png','Alea_2.png','Alea_3.png','Alea_4.png','Alea_5.png','Alea_6.png')
# Choosing random image from dice png
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Image label 
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack(expand=True)

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
# packing a widget in the parent widget 
ImageLabel.pack( expand=True)
# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage
# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
# pack a widget in the parent widget
button.pack( expand=True)

root.mainloop()