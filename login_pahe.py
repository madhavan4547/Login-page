import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == 'admin' and password == '12345':
        messagebox.showinfo('Login Success', 'Welcome, Admin!')
    else:
        messagebox.showerror('Login Failed', 'Invalid username or password')

# Create main window
root = tk.Tk()
root.title('Innovative Login Page')
root.geometry('600x400')
root.configure(bg='#282c34')

# Title Label
title_label = tk.Label(root, text='Login Portal', font=('Arial', 24, 'bold'), fg='white', bg='#282c34')
title_label.pack(pady=10)

# Description Label
description_label = tk.Label(root, text='Please enter your username and password to continue.\nAccess restricted to authorized users only.', font=('Arial', 12), fg='lightgray', bg='#282c34')
description_label.pack(pady=5)

# Frame for input fields
frame = tk.Frame(root, bg='#3c4048', padx=20, pady=20)
frame.pack(pady=20)

# Username label and entry
label_username = tk.Label(frame, text='Username:', font=('Arial', 16), fg='white', bg='#3c4048')
label_username.pack(pady=5)
entry_username = tk.Entry(frame, font=('Arial', 16), width=25)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(frame, text='Password:', font=('Arial', 16), fg='white', bg='#3c4048')
label_password.pack(pady=5)
entry_password = tk.Entry(frame, show='*', font=('Arial', 16), width=25)
entry_password.pack(pady=5)

# Login button
btn_login = tk.Button(root, text='Login', font=('Arial', 16), command=login, bg='#61afef', fg='white', padx=10, pady=5)
btn_login.pack(pady=10)

root.mainloop()

