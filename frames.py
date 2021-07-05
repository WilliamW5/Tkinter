from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames')
root.iconbitmap('Images\WillRagB.ico')

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)

# packs inside of the outside container
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click Here!")
b.pack()

root.mainloop()

