from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Database')
root.iconbitmap('Images/WillRagB.ico')
root.geometry('800x600')

# Database 

# Create a Database or connect to an existing one
conn = sqlite3.connect('address_book.db')

# Create Cursor: cursor executes commands and comes back with result
curs = conn.cursor()

# Create table: 
# datatypes in sqlite3: text, integers(whole), real(decimal), null, blob(image/video files)

#curs.execute("""CREATE TABLE addresses (
#    first_name text,
#    last_name text,
#    city text,
#    state text,
#    zipcode integer
#    )""")

# Create Submit Function for database
def submit():
    # Connect to the database
    conn = sqlite3.connect('address_book.db')
    # Create cursor for function
    curs = conn.cursor()
    

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Commit changes: after changes you want to commit
conn.commit()

# Close connection
conn.close()


root.mainloop()