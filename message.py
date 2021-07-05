from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message')
root.iconbitmap('Images/WillRagB.ico')

# different popups
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# askokcancel and askyesno return 1 or 0
# askquestion returns yes or no
# showerror, showwarning, and showifno returns ok

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You Clicked YES!").pack()
    else:
        Label(root, text="You Clicked NO!").pack()

Button(root,text="popup", command=popup).pack()

root.mainloop()