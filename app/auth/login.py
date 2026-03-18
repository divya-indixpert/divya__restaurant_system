from app.auth.signup import UserSystem

class Log(UserSystem):

    def login_user(self):
        self.read_file()

        name = input("Enter your name: ")
        password = input("Enter password: ")
        role = input("please reenter your role:")

        for user in self.users_list:
            if user["name"] == name and user["password"] == password and user["role"] == role:
                print("Login successful")
                print(f"Welcome {name}") 
                return

        print("Invalid username or password")