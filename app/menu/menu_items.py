from app.menu.item import show_menu
from app.menu.add_new_dish import add_item
from app.menu.update import update_item
from app.menu.delete import delete_item
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.GREEN + Style.BRIGHT + "\nWelcome to Restaurant Management System 🍽️")

def admin_menu():
    
    while True:

        print(Fore.MAGENTA + Style.BRIGHT + "\n===================================")
        print(Fore.YELLOW + Style.BRIGHT + "        🍴 ROYAL PLATE MENU 🍴     ")
        print(Fore.MAGENTA + Style.BRIGHT + "===================================")

        print(Fore.CYAN + "1. View Items")
        print(Fore.CYAN + "2. Add New Item")
        print(Fore.CYAN + "3. Update Item")
        print(Fore.CYAN + "4. Delete Item")
        print(Fore.CYAN + "5. Exit")

        print(Fore.MAGENTA + "===================================")

        choice = input(Fore.BLUE + " Enter your choice: ").strip()

      
        if not choice.isdigit():
            print(Fore.RED + " Please enter numbers only")
            continue

        if choice == "1":
            print(Fore.GREEN + "\n Showing Menu...")
            show_menu()

        elif choice == "2":
            print(Fore.YELLOW + "\n Add New Dish")
            add_item()

        elif choice == "3":
            print(Fore.YELLOW + "\n Update Dish")
            update_item()

        elif choice == "4":
            print(Fore.RED + "\n Delete Dish")
            delete_item()

        elif choice == "5":
            print(Fore.GREEN + Style.BRIGHT + "\n Thank you for using the system!")
            break

        else:
            print(Fore.RED + " Invalid choice, try again")