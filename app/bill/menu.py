from app.bill.final_bill import billing

def bill_menu():

    while True:
        print("\n===== BILL MENU =====")
        print("1. Generate Bill")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == 1:
            billing()

        elif choice == 2:
            break

        else:
            print("Invalid choice")