from colorama import Fore, Style, init
from app.bill.final_bill import billing

init(autoreset=True)

def bill_menu():

    while True:
        print(Fore.MAGENTA + Style.BRIGHT + "\n===== BILL MENU =====")
        print(Fore.CYAN + "1. Generate Bill")
        print(Fore.CYAN + "2. Exit")

        choice = input(Fore.WHITE + "Enter choice: ")
        if not choice.isdigit():
            print(Fore.RED + " Enter only number only (1 to 2)!")
            continue


        if choice == "1":
            print(Fore.GREEN + "\n Generating Bill...\n")
            billing()

        elif choice == "2":
            print(Fore.YELLOW + " Exiting Bill Menu...")
            break

        else:
            print(Fore.RED + " Invalid choice, try again")