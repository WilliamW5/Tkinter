from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning to Code")
# changes the icon in the title bar - does not work cause not .ico, its a jpg
root.iconbitmap('dnd.jpg')

my_img = ImageTk.PhotoImage(Image.open("dnd.jpg"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()