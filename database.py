from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Database')
root.iconbitmap('Images/WillRagB.ico')
root.geometry('370x600')

# Database

# Create a Database or connect to an existing one
conn = sqlite3.connect('address_book.db')

# Create Cursor: cursor executes commands and comes back with result
curs = conn.cursor()

# Create table:
# datatypes in sqlite3: text, integers(whole), real(decimal), null, blob(image/video files)
# curs.execute("""CREATE TABLE addresses (
#    first_name text,
#    last_name text,
#    address text,
#    city text,
#    state text,
#    zipcode integer
#    )""")

# Creates a save function for the update function


def save():
    # Connect to the database
    conn = sqlite3.connect('address_book.db')
    # Create cursor for function
    curs = conn.cursor()

    record_id = select_box.get()
    curs.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
                 {
                     'first': f_name_editor.get(),
                     'last': l_name_editor.get(),
                     'address': address_editor.get(),
                     'city': city_editor.get(),
                     'state': state_editor.get(),
                     'zipcode': zipcode_editor.get(),
                     'oid': record_id
                 })

    # Commit changes: after changes you want to commit
    conn.commit()
    # Close connection
    conn.close()

    editor.destroy()


# Create update function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title('Edit a Record')
    editor.iconbitmap('Images/WillRagB.ico')
    editor.geometry('370x200')

    # Connect to the database
    conn = sqlite3.connect('address_book.db')
    # Create cursor for function
    curs = conn.cursor()

    record_id = select_box.get()
    # Query the database
    curs.execute("SELECT * FROM addresses WHERE oid= " + record_id)
    records = curs.fetchall()

    # Create Global Variables for text box
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    # pady tuple means just pad 10-top 0-bot
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a Save edited Button
    save_button_editor = Button(editor, text="Update Record", command=save)
    save_button_editor.grid(row=11, column=0, columnspan=2,
                            pady=10, padx=10, ipadx=133)

    # Commit changes: after changes you want to commit
    conn.commit()
    # Close connection
    conn.close()


# Create function to delete record
def delete():
    # Connect to the database
    conn = sqlite3.connect('address_book.db')
    # Create cursor for function
    curs = conn.cursor()

    # Delete a record
    curs.execute("DELETE from addresses WHERE oid= " + select_box.get())

    # Commit changes: after changes you want to commit
    conn.commit()
    # Close connection
    conn.close()

    # Refreshes records
    query()

# Create Submit Function for database


def submit():
    # Connect to the database
    conn = sqlite3.connect('address_book.db')
    # Create cursor for function
    curs = conn.cursor()
    # 4 columns
    # Insert into Table, can also do cur.executemany("""INSERT INTO addresses VALUES(?,?,?,?)""", dictionary) adds multiple inserts
    curs.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                 {
                     'f_name': f_name.get(),
                     'l_name': l_name.get(),
                     'address': address.get(),
                     'city': city.get(),
                     'state': state.get(),
                     'zipcode': zipcode.get()
                 })

    # Commit changes: after changes you want to commit
    conn.commit()

    # Close connection
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create a query function
def query():
    # Connect to the database
    conn = sqlite3.connect('address_book.db')
    # Create cursor for function
    curs = conn.cursor()

    # Query the database
    curs.execute("SELECT *, oid FROM addresses")
    records = curs.fetchall()

    # Loop through results
    print_records = ''
    for record in records:
        # record would return all data. the below returns the first/last name and oid
        print_records += str(record[6]) + "  " + \
            str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, anchor='e', justify=LEFT, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes: after changes you want to commit
    conn.commit()

    # Close connection
    conn.close()


# Create text boxes
f_name = Entry(root, width=30)
# pady tuple means just pad 10-top 0-bot
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
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
select_box = Entry(root, width=30)
select_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
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
select_box_label = Label(root, text="Select ID")
select_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create a Delete Button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create an Update Button
edit_button = Button(root, text="Edit Record", command=edit)
edit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

# Commit changes: after changes you want to commit
conn.commit()

# Close connection
conn.close()


root.mainloop()
