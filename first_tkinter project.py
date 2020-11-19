# First tkinter test project for GUI

from tkinter import *
import os

'''
Changing later to connect to db(?)
change -> tkinter items -> tkinter canvas, frame, flace, mainloop instead
'''

#Key down function (events)
def click():
    entered_text=textentry.get() #call get on textbox var before
    output.delete(0.0, END)
#Main
window = Tk()
window.title("Test tkinter project")
window.configure(background = "lightblue")

#Photo
photo_1 = PhotoImage(file="Watashi-tachi Nagano Minami Alps.png")
photo_1 = photo_1.subsample(4,4) #Basic image mnpl, PIL/Image imports not found
Label (window, image=photo_1, bg="black") .grid(row=5, column=0, sticky='EWNS')
#(Sticky East or West > right or left)

#Create Label
Label (window, text = "Enter a word you want to study/review: ", bg="black", fg="white", font="none 12 bold") .grid(row=0, column=0, sticky='EWNS')

#Text Box
textentry = Entry(window, width=25, bg="white")
textentry.grid(row=1, column=0, sticky='EWNS')

#Submit (Buttons)
Button(window, text="SUBMIT", width=6, command=click) .grid(row=2,column=0, sticky='EWNS')

#Creating a text box
Label (window, text = "...and its definition is: ", bg="black", fg="white", font="none 12 bold") .grid(row=3, column=0, sticky='EWNS')

my_compdictionary = {} #To add, or fill 

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=4, column=0, sticky='EWNS')
