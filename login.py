from customtkinter import *
from PIL import Image
from tkinter import messagebox


def login():
    if userNameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif userNameEntry.get().lower() == 'munib' and passwordEntry.get() == 'Comirnatypfizer1!':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()

        import employee_management_system as ems
    else:
        messagebox.showerror('Error', 'Wrong credentials')


'''
Building the Login Page GUI
'''

root = CTk()  # Creates the login root

# root Geometry
root.geometry('736x414')
root.resizable(0, 0)  # Now you cannot change the root size after launching
root.title('Login Page')

# Retrieving Image
image_path = '2.jpg'
image = CTkImage(Image.open(image_path), size=(736, 414))

# Labeling Image onto the root
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)

# Putting the heading on the root
headingLabel = CTkLabel(root, text="Employee Management System", bg_color='#340B83', text_color='white',
                        font=('Goudy Old Style', 20, 'bold'))
headingLabel.place(x=20, y=100)

userNameEntry = CTkEntry(root, placeholder_text='Enter Your Username', width=150)
userNameEntry.place(x=50, y=150)

passwordEntry = CTkEntry(root, placeholder_text='Enter Your Password', width=150, show='*')
passwordEntry.place(x=50, y=200)

loginButton = CTkButton(root, text='Login', cursor='hand2', command=login)
loginButton.place(x=50, y=250)

root.mainloop()
