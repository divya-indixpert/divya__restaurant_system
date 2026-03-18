from auth.signup import UserSystem
from auth.login import Log

signup = UserSystem()
login = Log()

def details():
    while True:
        print("\033[34m===== USER MANAGEMENT SYSTEM =====\033[0m")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                signup.signup_user()

            elif choice == 2:
                login.login_user()

            elif choice == 3:
                print("Program closed")
                break

            else:
                print("Invalid choice")

        except:
            print("Please enter numbers only")
