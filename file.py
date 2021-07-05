from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('File Dialog')
root.iconbitmap('Images/WillRagB.ico')
root.geometry("800x600")

def open():
    global my_image
    global my_label
    global my_image_label
    # filetypes(("description", filetype), ())
    root.filename = filedialog.askopenfilename(initialdir="/Tkinter/Images/", title="Select A File", filetypes=((".png, .jpg", "*.png *.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.grid(row=1, column=0, columnspan=2)
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.grid(row=2, column=0, columnspan=2)



btn = Button(root, text="Open File", command=open)
btn.grid(row=0, column=0)

root.mainloop()