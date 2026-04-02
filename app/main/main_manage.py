from app.auth.manage import details
from app.table_booking.menu_booking import menu
from app.menu.menu_items import admin_menu
from app.bill.menu import billing

from colorama import Fore, Back, Style, init
init(autoreset=True)

def info():
    while True:

        try:
            print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "\n       THE ROYAL PLATE       ")
            print(Fore.CYAN + "="*40)

            print(Fore.LIGHTGREEN_EX + "➤ 1. Guest Management")
            print(Fore.LIGHTBLUE_EX + "➤ 2. Table Reservations")
            print(Fore.LIGHTMAGENTA_EX + "➤ 3. Food Menu")
            print(Fore.LIGHTYELLOW_EX + "➤ 4. Billing & Checkout")
            print(Fore.LIGHTRED_EX + "➤ 5. Exit")

            print(Fore.CYAN + "="*40)

            choice = int(input(Fore.WHITE + Style.BRIGHT + "Enter your choice ➤ "))
            
            if not choice.isdigit():
                print(Fore.RED + " Enter only number only (1 to 3)!")
                continue


            if choice == 1:
                print(Fore.GREEN + "✔ Opening Guest Management...\n")
                details()

            elif choice == 2:
                print(Fore.GREEN + "✔ Opening Table Reservation...\n")
                menu()

            elif choice == 3:
                print(Fore.GREEN + "✔ Opening Food Menu...\n")
                admin_menu()

            elif choice == 4:
                print(Fore.GREEN + "✔ Opening Billing System...\n")
                billing()

            elif choice == 5:
                print(Fore.RED + Style.BRIGHT + " Program Closed")
                break
            else:
                print(Fore.RED + "⚠ Invalid choice")

        except ValueError:
            print(Fore.RED + "⚠ Please enter numbers only")

