from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning to Code")
root.iconbitmap('dnd.jpg')

# set images to variables
my_img1 = ImageTk.PhotoImage(Image.open("images/test1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/test2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/test3.jpg"))

# add variables to list (array)
image_list = [my_img1, my_img2, my_img3]

# bd = border, relief = "depth" into pane, anchor(E) anchors the label to the right side
status = Label(root, text="Image 1 of " + str(len(image_list)), bd= 1, relief=SUNKEN, anchor=E)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image= image_list[image_number - 1])
	button_forward = Button(root, text= ">>", command= lambda: forward(image_number + 1))
	button_back = Button(root, text= "<<", command= lambda: back(image_number - 1))
	
	if image_number == len(image_list):
		button_forward = Button(root, text= ">>", state= DISABLED)

	my_label.grid(row= 0, column= 0, columnspan= 3)
	button_back.grid(row= 1, column= 0)
	button_forward.grid(row= 1, column= 2)
	status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd= 1, relief=SUNKEN, anchor=E)
	status.grid(row= 2, column= 0, columnspan= 3, sticky=W+E)


def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image= image_list[image_number - 1])
	button_forward = Button(root, text= ">>", command= lambda: forward(image_number + 1))
	button_back = Button(root, text= "<<", command= lambda: back(image_number - 1))

	if image_number == 1:
		button_back = Button(root, text= "<<", state= DISABLED)

	my_label.grid(row= 0, column= 0, columnspan= 3)
	button_back.grid(row= 1, column= 0)
	button_forward.grid(row= 1, column= 2)

	status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd= 1, relief=SUNKEN, anchor=E)
	status.grid(row= 2, column= 0, columnspan= 3, sticky=W+E)



# sets label to the image
my_label = Label(image=my_img1)
my_label.grid(row= 0, column= 0, columnspan= 3)

# create buttons and add them to root
# pass something through a button comand, you MUST to Lambda
button_back = Button(root, text= "<<", command= back, state= DISABLED)
button_exit = Button(root, text= "Exit Program", command= root.quit)
button_forward = Button(root, text= ">>", command= lambda: forward(2))

# changes location of buttons
button_back.grid(row= 1, column= 0)
button_exit.grid(row= 1, column= 1)
button_forward.grid(row= 1, column= 2, pady= 10)
# pad to give space to status
# sticky W+E, stretches the label from left to right
status.grid(row= 2, column= 0, columnspan= 3, sticky=W+E)

root.mainloop()