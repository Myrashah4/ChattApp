class ServerProxy:
    def __init__(self):
        self.connection = None
        self.users = [("admin", "admin123"), ("alex31", "alex123")]

    def connect(self, host, port) -> bool:
        return True

    def getConnectedUsers(self):
        # To do in the future we will send a real text command to server via self.connection,
        # receive raw text which we will parse with another function from another submodule or class
        return ["Alex", "Sofia", "Fred"]

    def sendMessageToUser(self, user: str, message: str) -> None:
        # To do in the future we will send a real text command to server via self.connection
        return None

    def createUserAccount(self, username: str, password: str):
        for input_username in self.users:
            if username == input_username:
                return False  # username already exists
        self.users.append((username, password))
        return True

    def checkingLoginInfo(self, username: str, password: str):
        for input_username, input_password in self.users:
            if username == input_username and password == input_password:
                return True
        return False