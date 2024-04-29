from ChatApp_main_window import *
from ServerProxy import *
from login_interface import *

server = ServerProxy()


def main():
    while True:
        answer = createLoginWindow(server)
        if answer[0]:
            chatappMainWindow(server, answer[1])
            break  # Exit the loop if successfully logged in
        else:
            break  # Exit the loop if login is not successful


if __name__ == "__main__":
    main()
