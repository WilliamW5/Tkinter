from tkinter import *

root = Tk()

# Entry = TextFields
e = Entry(root, width=50, bg="#ffffff", fg="#000000", borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name",command=myClick)
myButton.pack()

root.mainloop()
