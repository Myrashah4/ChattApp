import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askquestion

exit_var = False


def login_clicked(server, username, password, root):
    if server.checkingLoginInfo(username, password):
        root.destroy()  # if login successful -> cancelling the login window
        global exit_var
        exit_var = True
        return True
    else:
        msg = "Cannot Login"
        showinfo(title="Information", message=msg)
    return False


def register_window(server, root):
    root.destroy()  # destroying the login window to show register window
    from create_account_interface import createAccountWindow
    createAccountWindow(server)

    # when exit button was clicked
def exit_confirmation(root):
    answer = askquestion("Quit", "Are you sure you want to exit?")
    if answer == "Yes":
        root.destroy()

def createLoginWindow(server):
    # login window
    root = tk.Tk()
    root.title("Chat App")
    root.geometry("400x300")

    ttk.Label(root, text="Login To Existing Account.").pack()

    # store username and password
    username = tk.StringVar()
    password = tk.StringVar()

    # login frame
    frame = ttk.Frame(root, padding="20")
    frame.pack(fill=tk.BOTH, expand=True)

    # entering username
    ttk.Label(frame, text="Username: ").grid(row=0, column=0, sticky="w")
    username_input = ttk.Entry(frame)
    username_input.grid(row=0, column=1, sticky="we")

    # entering password
    ttk.Label(frame, text="Password: ").grid(row=1, column=0, sticky="w")
    password_input = ttk.Entry(frame, show="*")
    password_input.grid(row=1, column=1, sticky="we")

    # login button
    login_button = ttk.Button(frame, text="Login",
                              command=lambda: login_clicked(server, username.get(), password.get(), root))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    # register button
    register_button = ttk.Button(frame, text="Create New Account", command=lambda: register_window(server, root))
    register_button.grid(row=3, column=0, columnspan=2, pady=10)

    # exit button
    exit_button = ttk.Button(frame, text="Exit", command=lambda: exit_confirmation(root))
    exit_button.grid(row=4, column=0, columnspan=2, pady=10)

    # if user clicks return key, the function login_clicked is called with the current values of username and password
    root.bind('<Return>', lambda event: login_clicked(server, username.get(), password.get(), root))

    root.mainloop()
    return exit_var, username.get()

