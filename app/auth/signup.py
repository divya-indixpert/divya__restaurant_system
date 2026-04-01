import json
from getpass import getpass

class UserSystem:

    def __init__(self):
        self.users_list = []

    def signup_user(self):
        self.read_file()

        print("\n\033[36m===== SIGNUP =====\033[0m")  

        while True:
            user_name = input("\033[34mEnter your name: \033[0m")
            if not user_name.isalpha():
                print("\033[31mInvalid name! Only alphabets allowed\033[0m")
            else:
                break

        while True:
            password = getpass("\033[34mEnter your password: \033[0m")
            if len(password) < 8:
                print("\033[31mPassword must be at least 8 characters\033[0m")
            else:
                break

        while True:
            email = input("\033[34mEnter your email: \033[0m")
            if "@" not in email or "." not in email:
                print("\033[31mInvalid email format\033[0m")
            else:
                break

        while True:
            role = input("\033[34mEnter role (Admin/Staff): \033[0m")
            if role.lower() not in ["admin", "staff"]:
                print("\033[31mInvalid role! Enter Admin or Staff\033[0m")
            else:
                break

        for user in self.users_list:
            if user["name"].lower() == user_name.lower():
                print("\033[31mUser already exists\033[0m")
                return

        user_data = {
            "name": user_name,
            "password": password,
            "email": email,
            "role": role
        }

        self.users_list.append(user_data)
        self.write_file()

        print("\033[32mAccount created successfully\033[0m")  

    def read_file(self):
        try:
            with open("app/dashboard/users.json", "r") as file:
                self.users_list = json.load(file)
        except:
            self.users_list = []

    def write_file(self):
        with open("app/dashboard/users.json", "w") as file:
            json.dump(self.users_list, file, indent=4)