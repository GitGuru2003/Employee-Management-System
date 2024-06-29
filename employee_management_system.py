from customtkinter import *
from PIL import Image
from tkinter import messagebox
from tkinter import ttk

window = CTk()

# Window Geometry
window.geometry('930x580')
window.resizable(False, False)  # Now you cannot change the window size after launching
window.title('Employee Management System')
window.configure(fg_color='#1E1D1D')

logo = CTkImage(Image.open('office.jpg'), size=(930, 158))

# Labeling Image onto the window
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

# Dividing the space into two frames
leftFrame = CTkFrame(window, fg_color='#1E1D1D')
leftFrame.grid(row=1, column=0)

# ID Label and Entry
idLabel = CTkLabel(leftFrame, text='ID', font=('arial', 18, 'bold'), text_color='white')
idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)

idEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1)

# Name Label and Entry
nameLabel = CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'), text_color='white')
nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)

nameEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
nameEntry.grid(row=1, column=1)

# Phone Label and Entry
phoneLabel = CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'), text_color='white')
phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)

phoneEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
phoneEntry.grid(row=2, column=1)

# Role Label
roleLabel = CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white')
roleLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)

role_options = ['Web Developer', 'Cloud Architect', 'Technical Writer', 'Network Engineer', 'Data Scientist', 'DevOps Engineer', 'Business Analyst', 'IT Consultant', 'UX/UI Designer']
roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=('arial', 15, 'bold'), state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])

# Gender Label
genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white')
genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)

gender_options = ['Male', 'Female']
genderBox = CTkComboBox(leftFrame, values=gender_options, width=180, font=('arial', 15, 'bold'), state='readonly')
genderBox.grid(row=4, column=1)
genderBox.set(gender_options[0])

# Salary Label
salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white')
salaryLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)

salaryEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
salaryEntry.grid(row=5, column=1)

# Right Frame
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)

# Adding things to the right frame
search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchBox = CTkComboBox(rightFrame, values=search_options, state='readonly')
searchBox.grid(row=0, column=0)
searchBox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1)

searchButton = CTkButton(rightFrame, text='Search', width=100)
searchButton.grid(row=0, column=2)

showAllButton = CTkButton(rightFrame, text='Show All', width=100)
showAllButton.grid(row=0, column=3, pady=5)

# Treeview with Scrollbar
treeScroll = ttk.Scrollbar(rightFrame)
treeScroll.grid(row=1, column=4, sticky='ns')

tree = ttk.Treeview(rightFrame, height=13, yscrollcommand=treeScroll.set)
tree.grid(row=1, column=0, columnspan=4)
treeScroll.config(command=tree.yview)

tree['columns'] = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings')

tree.column('Id', width=50)
tree.column('Name', width=150)
tree.column('Phone', width=100)
tree.column('Role', width=150)
tree.column('Gender', width=70)
tree.column('Salary', width=100)

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 18, 'bold'))

buttonFrame = CTkFrame(window, fg_color='#1E1D1D')
buttonFrame.grid(row=2, column=0, columnspan=2)

newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15)
newButton.grid(row=0, column=0, pady=5)

addButton = CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15)
addButton.grid(row=0, column=1, pady=5, padx=5)

updateButton = CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15)
updateButton.grid(row=0, column=2, pady=5, padx=5)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15)
deleteButton.grid(row=0, column=3, pady=5, padx=5)

deleteAllButton = CTkButton(buttonFrame, text='Delete All', font=('arial', 15, 'bold'), width=160, corner_radius=15)
deleteAllButton.grid(row=0, column=4, pady=5, padx=5)

window.mainloop()
