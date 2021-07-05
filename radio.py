from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')
root.iconbitmap('Images/WillRagB.ico')

MODES = [
    # "Label", "Value"
    # for the examble: 
    # (Toppings, Value)
    ("Pepperoni", "Pepperoni"),
    ("Peppers", "Peppers"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for toppings, value in MODES:
    Radiobutton(root, text=toppings, variable=pizza, value=value, anchor=W).pack()


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# allows us not have to use test.get()
# Can also do test = StringVar, if you wanted a string variable
#test = IntVar()
#test.set(2)
# tkinter variables
#Radiobutton(root, text="Option 1", variable=test, value=1, command=lambda: clicked(test.get())).pack()
#Radiobutton(root, text="Option 2", variable=test, value=2, command=lambda: clicked(test.get())).pack()
#myLabel = Label(root, text=test.get())
#myLabel.pack()
#myButton = Button(root, text="Click", command=lambda: clicked(test.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click", command=lambda: clicked(pizza.get())).pack()


root.mainloop()