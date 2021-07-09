from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Slider')
root.iconbitmap('Images/WillRagB.ico')
root.geometry("800x600")

# make sure you pack on another line
vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
	my_label = Label(root, text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# can put command=slide in slider
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Click Me!", command=slide).pack()


root.mainloop()