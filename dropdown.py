from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('DropDown')
root.iconbitmap('Images/WillRagB.ico')
root.geometry('800x600')

def show():
    myLabel = Label(root, text=var.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]

var =StringVar()
var.set(options[0])

# use a star in front of the list (options)
drop = OptionMenu(root, var, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show)
myButton.pack()

root.mainloop()