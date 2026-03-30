from app.auth.signup import UserSystem

class Log(UserSystem):

    def login_user(self):
        self.read_file()

        name = input("Enter your name: ")
        password = input("Enter password: ")
        role = input("Please re-enter your role: ")

        for user in self.users_list:
            if (
                user["name"].lower() == name.lower()
                and user["password"] == password
                and user["role"].lower() == role.lower()
            ):
                print("Login successful")
                print(f"Welcome {name}")
                return

        print("Invalid username or password")