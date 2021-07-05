from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('New Window')
root.iconbitmap('Images/WillRagB.ico')

btn = Button(root, text="open new window", command=open)

def open():
    global my_img
    top = Toplevel()
    top.title('the top window')
    top.iconbitmap('Images/WillRagB.ico')
    my_img = ImageTk.PhotoImage(Image.open("Images/test2.jpg"))
    lbl = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close", command=top.destroy).pack()


btn = Button(root, text="open new window", command=open).pack()

root.mainloop()