from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames')
root.iconbitmap('Images\WillRagB.ico')

# puts padding inside of the frame
frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)

# packs inside of the outside container
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...Or Here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()

