import getpass
import logging
import re
from app.auth.signup import UserSystem

logging.basicConfig(
    filename="app/dashboard/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Log(UserSystem):

    def login_user(self):
        self.read_file()

     
        while True:
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty!")
                logging.warning("Login failed: Empty name")
            elif not name.isalpha():
                print("Name should contain only alphabets")
                logging.warning(f"Invalid name input: {name}")
            else:
                break

        while True:
            email = input("Enter your email: ").strip()
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            if not re.match(email_pattern, email):
                print("Invalid email format!")
                logging.warning(f"Invalid email input: {email}")
            else:
                break

       
        password = getpass.getpass("Enter password: ").strip()

   
        while True:
            role = input("Enter your role (Admin/Staff): ").strip()
            if role.lower() not in ["admin", "staff"]:
                print("Invalid role! Enter Admin or Staff")
                logging.warning(f"Invalid role input: {role}")
            else:
                role = role.capitalize()
                break

      
        for user in self.users_list:
            if (
                user["name"].lower() == name.lower()
                and user["email"].lower() == email.lower()
                and user["password"] == password
                and user["role"].lower() == role.lower()
            ):
                print("\nLogin successful ")
                print(f"Welcome {name} ({role})")

                logging.info(f"User login successful: {name} ({role})")
                return

        print("\n Invalid username, email, password, or role")
        logging.error(f"Login failed for user: {name}")