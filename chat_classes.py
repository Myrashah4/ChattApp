class ChatApp:
    def __init__(self):
        self.users = {}
        self.logged_in_users = {}

    def addFriend(self, username, friend_username):

    def getChatType(self):

    def setChatType(self):

class Message:
    def __init__(self, sender, content, message_type):
        self.sender = sender
        self.content = content
        self.message_type = message_type

    def getType(self):

    def setType(self):

    def sendTextMessage(self):

    def sendPhoto(self):

    def getMessages(self, messages):

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.friends = []
        self.messages = []

    def createAccount(self, username, password):

    def login(self, username, password):

    def logout(self):

    def chat(self, username):

    def viewSettings(self):

    def search(self):

    def getNotifications(self):

class Settings:
    def __init__(self):
        self.notification = 'sound'
        self.privacy = {'profile_picture': True}
        self.language = 'english'
        self.account_security = {'password': ''}

    def viewProfile(self):

    def setNotifications(self):

    def updateImage(self, new_image):

    def changePassword(self, new_password):

    def changeNumber(self, new_number):

class Admin:

    def __init__(self):
        self.admin_username = "admin"
        self.admin_password = "admin123"

    def login(self, username, password):

    def deleteUser(self, chat_app, username): #might be useful, but not sure if we will implement this

    def viewAccount(self, username):


def main():
    chat_app = ChatApp()
    admin = Admin()
    logged_in_user = None

    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Logout")
        print("4. Chat")
        print("5. View Settings")
        print("6. Search")
        print("7. View Notifications")
        print("8. Admin Login")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            chat_app.createAccount(username, password)

        elif choice == "2":
            if logged_in_user:
                print("Already logged in.")
                continue
            username = input("Enter username: ")
            password = input("Enter password: ")
            chat_app.login(username, password)
            logged_in_user = username

        elif choice == "3":
            if logged_in_user:
                chat_app.logout()
                logged_in_user = None
            else:
                print("You are not logged in.")

        elif choice == "4":
            if logged_in_user:
                username = input("Enter username to chat: ")
                chat_app.sendTextMessage(username)
                chat_app.sendPhoto(username)
            else:
                print("Please log in first.")

        elif choice == "5":
            if logged_in_user:
                chat_app.viewSettings()
            else:
                print("Please log in first.")

        elif choice == "6":
            if logged_in_user:
                chat_app.search()
            else:
                print("Please log in first.")

        elif choice == "7":
            if logged_in_user:
                chat_app.getNotifications()
            else:
                print("Please log in first.")

        elif choice == "8":
            if not logged_in_user:
                admin_username = input("Enter admin username: ")
                admin_password = input("Enter admin password: ")
                if admin.login(admin_username, admin_password):
                    print("Admin logged in successfully.")
                else:
                    print("Invalid admin credentials.")
            else:
                print("Please log out before admin login.")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()