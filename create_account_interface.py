import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from login_interface import createLoginWindow


def create_account_clicked(server, v_username, v_password, v_confirm_password, root1):
    username_input = v_username.get()
    password_input = v_password.get()
    confirm_password = v_confirm_password.get()

    # Check if email and password are provided
    if not username_input or not password_input:
        showinfo(title="Information", message="Enter both username and password in order to create new account.")
        return

    # Check if password and confirm password match
    if password_input != confirm_password:
        showinfo(title="Information", message="Password and confirmed password do not match.")
        return

    success = server.registerUser(username_input, password_input)
    if success:
        showinfo(title="Information", message="Successfully created new account.")
        root1.destroy()  # exit registration window after successfully registering
        createLoginWindow(server)  # call the login window
    else:
        showinfo(title="Information", message="Username already exists, please enter new username.")


def createAccountWindow(server):
    # register window
    root1 = tk.Tk()
    root1.title("Create New Account")
    root1.geometry("400x300")  # pixels x pixels

    ttk.Label(root1, text="Please enter your username and password to create new account.").pack()

    # store new username and password
    v_username = tk.StringVar()
    v_password = tk.StringVar()

    frame = ttk.Frame(root1, padding="20")
    frame.pack(fill=tk.BOTH, expand=True)

    # entering username
    ttk.Label(frame, text="Username:").grid(row=0, column=0, sticky="w")  # align to left
    username_input = ttk.Entry(frame)
    username_input.grid(row=0, column=1, sticky="we")  # stretch horizontally

    # entering password
    ttk.Label(frame, text="New Password:").grid(row=1, column=0, sticky="w")
    password_input = ttk.Entry(frame, show="*")
    password_input.grid(row=1, column=1)

    # confirming password
    ttk.Label(frame, text="Confirm New Password:").grid(row=2, column=0, sticky="w")
    confirm_new_password = ttk.Entry(frame, show="*")
    confirm_new_password.grid(row=2, column=1, sticky="we")

    # register button
    create_account_button = ttk.Button(frame, text="Register", command=lambda: create_account_clicked(server, v_username, v_password, confirm_new_password, root1))
    create_account_button.grid(row=3, column=0, columnspan=2, pady=10)

    # cancel button
    cancel_button = ttk.Button(frame, text="Cancel", command=lambda: [root1.destroy(), createLoginWindow(server)])
    cancel_button.grid(row=4, column=0, columnspan=2, pady=10)
