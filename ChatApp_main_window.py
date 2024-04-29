import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askquestion

def chatappMainWindow(server, username):
    root = tk.Tk()
    root.title("ChatApp")

    def send_message():
        message = message_entry.get()
        if message:
            # Code to send message to the server
            chat_text.config(state=tk.NORMAL)
            chat_text.insert(tk.END, f"{username}: {message}\n")
            chat_text.config(state=tk.DISABLED)
            message_entry.delete(0, tk.END)

    def exitConfirmation():
        input = askquestion("Quit", "Are you sure you want to exit?")
        if input.lower() == "yes":
            root.destroy()

    # Menu bar
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=exitConfirmation)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    # List of connected usernames
    connected_users_frame = ttk.Frame(root)
    connected_users_frame.pack(side=tk.LEFT, fill=tk.Y)

    ttk.Label(connected_users_frame, text="Connected Users").pack()
    users_listbox = tk.Listbox(connected_users_frame)
    users_listbox.pack(fill=tk.BOTH, expand=True)

    # Chat area
    chat_frame = ttk.Frame(root)
    chat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    chat_text = tk.Text(chat_frame, wrap="word")
    chat_text.pack(fill=tk.BOTH, expand=True)
    chat_text.config(state=tk.DISABLED)

    # Entry for typing messages
    message_entry = ttk.Entry(chat_frame)
    message_entry.pack(fill=tk.X, pady=5)
    message_entry.bind("<Return>", lambda event: send_message)

    send_button = ttk.Button(chat_frame, text="Send", command=send_message)
    send_button.pack(pady=5)

    # Display the username
    username_label = ttk.Label(chat_frame, text="Logged in as: " + username)
    username_label.pack(side="right", padx=5, pady=5)

    root.mainloop()