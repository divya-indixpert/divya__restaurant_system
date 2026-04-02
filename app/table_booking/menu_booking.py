from app.table_booking.booking import table_book
from app.table_booking.cancel import cancel_booking
from colorama import Fore, Style, init

init(autoreset=True)

def menu():
    try:
        while True:
            print(Fore.MAGENTA + Style.BRIGHT + "\n========== 🍽️ TABLE BOOKING ==========")
            print(Fore.CYAN + "1️⃣  Book Table")
            print(Fore.YELLOW + "2️⃣  Cancel Booking")
            print(Fore.RED + "3️⃣  Exit")
            print(Fore.MAGENTA + "======================================")

            choice = input(Fore.BLUE + " Enter choice: ").strip()

            if not choice.isdigit():
                print(Fore.RED + " Enter only number only (1 to 3)!")
                continue

            if choice == "1":
                print(Fore.GREEN + "\n Opening Table Booking...")
                table_book()

            elif choice == "2":
                print(Fore.YELLOW + "\n Opening Cancel Booking...")
                cancel_booking()

            elif choice == "3":
                print(Fore.GREEN + Style.BRIGHT + "\n Exiting Table Booking Menu...")
                break  

            else:
                print(Fore.RED + " Invalid choice, try again")

    except Exception as e:
        print(Fore.RED + f" Error: {e}")