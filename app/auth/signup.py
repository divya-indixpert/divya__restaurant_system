import json

class UserSystem:

    def __init__(self):
        self.users_list = []

    def signup_user(self):
        self.read_file()

        while True:
            user_name = input("Please enter your name: ")
            if not user_name.replace(" ", "").isalpha():
                print("Invalid name! Please enter only alphabets.")
            else:
                break

        while True:
            password = input("Please enter your password: ")
            if len(password) < 8:
                print("Password must be at least 8 characters long")
            else:
                break

        while True:
            email = input("Please enter your email: ")
            if "@" not in email or "." not in email:
                print("Invalid email format, try again")
            else:
                break

        while True:
            role = input("Please select your role (Admin/Staff): ")
            if role.lower() not in ["admin", "staff"]:
                print("Invalid role! Enter Admin or Staff")
            else:
                break

        for user in self.users_list:
            if user["name"] == user_name:
                print("User already exists")
                return

        user_data = {
            "name": user_name,
            "password": password,
            "email": email,
            "role": role
        }

        self.users_list.append(user_data)

        self.write_file()

        print("Account created successfully")

    def read_file(self):
        try:
            with open("users.json", "r") as file:
                self.users_list = json.load(file)
        except:
            self.users_list = []

    def write_file(self):
        with open("users.json", "w") as file:
            json.dump(self.users_list, file, indent=4)