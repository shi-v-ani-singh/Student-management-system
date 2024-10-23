# importing modules
from tkinter import *
import datetime
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

# connecting to the database

connector = mysql.connector.connect(host='localhost',user="root", passwd="",database="kryptora2")
cursor = connector.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS STUDENT_MANAGEMENT (
    STUDENT_ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(255),
    EMAIL VARCHAR(255),
    PHONE_NO VARCHAR(10),
    GENDER VARCHAR(10),
    DOB DATE,
    STREAM VARCHAR(255)
)
"""
cursor.execute(create_table_query)


def add_record():
    global name_var, email_var, contact_var, gender_var, dob, stream_var
    name = name_var.get()
    email = email_var.get()
    contact = contact_var.get()
    gender = gender_var.get()
    DOB = dob.get()
    stream = stream_var.get()
    if not name or not email or not contact or not gender or not DOB or not stream:
        messagebox.showerror('Error!', "Please enter all the details!")
    elif not contact.isdigit() or len(contact) != 10:
        messagebox.showerror('Wrong type', 'The contact no should be 10 digits and contain only numbers!')

    else:
        try:
            cursor.execute(
                'INSERT INTO STUDENT_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (%s, %s, %s, %s, %s, %s)',
                (name, email, contact, gender, DOB, stream))
            connector.commit()
            messagebox.showinfo('Record inserted', "Record of {} is added".format(name))
            reset_record()
            display_records()
        except Exception as e:
            messagebox.showerror('Database error', f"An error occurred: {e}")


def remove_record():
    if not tree.selection():
        messagebox.showerror('error!', "please select an item from database")
    else:
        # focusing on the row of database at which user has selected and storing it to current_item selected
        current_item = tree.focus()
        # item is a method in Treeview class of ttk module
        values = tree.item(current_item)
        selection = values["values"]
        tree.delete(current_item)
        cursor.execute('DELETE FROM STUDENT_MANAGEMENT WHERE STUDENT_ID=%d' % selection[0])
        connector.commit()
        messagebox.showinfo('Done', "the record is deleted successfully.")
        display_records()


def reset_record():
    global name_var, email_var, contact_var, gender_var, stream_var
    for i in ["name_var", "email_var", "contact_var", "gender_var", "stream_var"]:
        exec(f"{i}.set(' ')")
    # resetting dob to current date
    dob.set_date(datetime.datetime.now().date())


def remove_db():
    global tree
    tree.delete(*tree.get_children())
    reset_record()


def display_records():
    tree.delete(*tree.get_children())
    cursor.execute('select * from STUDENT_MANAGEMENT')
    data = cursor.fetchall()
    for records in data:
        tree.insert('', END, values=records)

def view_record():
    pass


# creating the gui window
root = Tk()
root.title("Student Management System")
# root.geometry('1000x800')
# root.resizable(0, 0)
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))
# left_frame background

lf_bg = 'lavender'

# creating the variables for the student detail

name_var = StringVar()
email_var = StringVar()
contact_var = StringVar()
gender_var = StringVar()
stream_var = StringVar()

# placing the components  into the root window
label_head = Label(root, text='STUDENT MANAGEMENT SYSTEM', font='Arial', bg='navajo white')
label_head.pack(side=TOP, fill=X)
# creating left and right frame
l_frame = Frame(root, bg=lf_bg)
l_frame.place(x=0, y=30, height=780, width=600)
r_frame = Frame(root, bg='salmon')
r_frame.place(x=400, y=30, height=710, width=950)

# left_frame components
Label(l_frame, text="Name :", bg=lf_bg).place(x=30, y=50)
Label(l_frame, text="Contact :", bg=lf_bg).place(x=30, y=100)

Label(l_frame, text="Email :", bg=lf_bg).place(x=30, y=150)
Label(l_frame, text="Gender :", bg=lf_bg).place(x=30, y=200)
Label(l_frame, text="DOB :", bg=lf_bg).place(x=30, y=250)
Label(l_frame, text="Stream :", bg=lf_bg).place(x=30, y=300)
Entry(l_frame, textvariable=name_var).place(x=170, y=50)
Entry(l_frame, textvariable=contact_var).place(x=170, y=100)
Entry(l_frame, textvariable=email_var).place(x=170, y=150)
Entry(l_frame, textvariable=stream_var).place(x=170, y=300)
OptionMenu(l_frame, gender_var, 'Male', 'Female').place(x=170, y=200, width=70)
dob = DateEntry(l_frame, width=15)
dob.place(x=180, y=250)
Button(l_frame, text='Submit', bg='white smoke', command=add_record).place(x=150, y=380)

# other buttons in left frame
Button(l_frame, text='Delete Record', bg='white smoke',command=remove_record).place(x=30, y=450)
Button(l_frame, text='View Record',bg='white smoke', command=view_record).place(x=200, y=450)
Button(l_frame, text='Clear Record', bg='white smoke',command=reset_record).place(x=30, y=520)
Button(l_frame, text='Remove DB ', bg='white smoke',command=remove_db).place(x=200, y=520)

# components of right frame
Label(r_frame, text='Students Record', font='300',bg='lavender').pack(side=TOP, fill=X)

# ttk library helps us to display data in both tabular and hierarchical form
# creating a table to show all the student record
columns = ('Student_ID', 'Name', 'Email Address', 'Contact No', 'Gender', 'Date of Birth', 'Stream')

tree = ttk.Treeview(r_frame, selectmode=BROWSE, columns=columns)
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

tree.heading('Student_ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Contact No', text='Phone No',anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)

tree.column('#0', width=0, anchor=CENTER,stretch=NO)
tree.column('#1', width=40, anchor=CENTER, stretch=NO)
tree.column('#2', width=120,anchor=CENTER, stretch=NO)
tree.column('#3', width=180, anchor=CENTER, stretch=NO)
tree.column('#4', width=60, anchor=CENTER,stretch=YES)
tree.column('#5', width=60, anchor=CENTER,stretch=NO)
tree.column('#6', width=70, anchor=CENTER,stretch=NO)
tree.column('#7', width=120,anchor=CENTER, stretch=YES)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()

root.update()
root.mainloop()

