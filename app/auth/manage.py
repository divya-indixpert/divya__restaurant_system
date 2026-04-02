from app.auth.signup import UserSystem
from app.auth.login import Log
from colorama import Fore, Style, init

init(autoreset=True)

signup = UserSystem()
login = Log()

def details():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n" + "═"*50)
        print(Fore.YELLOW + Style.BRIGHT + "      USER MANAGEMENT SYSTEM ".center(50))
        print(Fore.CYAN + "═"*50)

        print(Fore.GREEN + "➤ 1. Signup")
        print(Fore.BLUE + "➤ 2. Login")
        print(Fore.RED + "➤ 3. Exit")

        print(Fore.CYAN + "-"*50)

        choice = input(Fore.WHITE + Style.BRIGHT + "Enter your choice ➤ ").strip()

        if not choice.isdigit():
            print(Fore.RED + " Enter only number only (1 to 3)!")
            continue

        if choice == "1":
            print(Fore.GREEN + "\n Opening Signup...\n")
            signup.signup_user()

        elif choice == "2":
            print(Fore.BLUE + "\n Opening Login...\n")
            login.login_user()

        elif choice == "3":
            print(Fore.RED + Style.BRIGHT + "\n Program Closed")
            print(Fore.CYAN + "═"*50)
            break

        else:
            print(Fore.RED + " Invalid choice")