from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Checkboxes')
root.iconbitmap('Images/WillRagB.ico')
root.geometry("800x600")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check Here", variable= var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()