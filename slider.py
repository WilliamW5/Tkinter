from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Slider')
root.iconbitmap('Images/WillRagB.ico')
root.geometry("800x600")

def slide(value):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

# make sure you pack on another line
vertical = Scale(root, from_=0, to=200)
vertical.pack()

# can put command=slide in slider
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text="Clicl me", command=slide).pack()

root.mainloop()