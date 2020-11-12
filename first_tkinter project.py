# First tkinter test project for GUI

from tkinter import *

#Main
window = Tk()
window.title("Test tkinter project")

#Photo
photo_1 = PhotoImage(file="Watashi-tachi Nagano Minami Alps.png")
Label (window, image=photo_1, bg="black") .grid(row=0, column=0, sticky=E)
