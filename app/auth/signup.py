import json
import re
from getpass import getpass
from app.utils.logger import get_logger  

logger = get_logger()   

class UserSystem:

    def __init__(self):
        self.users_list = []

    def signup_user(self):
        self.read_file()

        print("\n===== SIGNUP =====")

      
        while True:
            user_name = input("Enter your name: ")
            if not user_name.isalpha():
                print("Invalid name! Only alphabets allowed")
            else:
                break

    
        while True:
            password = getpass("Enter your password: ")
            if len(password) < 8:
                print("Password must be at least 8 characters")
            else:
                break

        while True:
            email = input("Enter your email: ").strip()

            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            if not re.match(email_pattern, email):
                print("Invalid email! Example: abc123@gmail.com")
                logger.warning(f"Invalid email entered: {email}")
            else:
                break

       
        while True:
            role = input("Enter role (Admin/Staff): ")
            if role.lower() not in ["admin", "staff"]:
                print("Invalid role! Enter Admin or Staff")
            else:
                break

        for user in self.users_list:
            if user["name"].lower() == user_name.lower():
                print("User already exists")
                logger.warning(f"Signup FAILED - User already exists: {user_name}")
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

        logger.info(f"Signup SUCCESS - User: {user_name}, Role: {role}, Email: {email}")

    def read_file(self):
        try:
            with open("app/dashboard/users.json", "r") as file:
                self.users_list = json.load(file)
        except:
            self.users_list = []

    def write_file(self):
        with open("app/dashboard/users.json", "w") as file:
            json.dump(self.users_list, file, indent=4)