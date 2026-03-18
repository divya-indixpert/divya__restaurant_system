from auth.manage import details
from menu.menu_items import admin_menu
from bill.menu import bill_menu
def info():
    while True:
        print("\n========= MAIN MENU =========")
        print("1. User Management")
        print("2. Restaurant Menu")
        print("3. Bill System")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                details()
                  
            elif choice == 2:
                admin_menu()
            
            elif choice == 3:
                bill_menu()
                
            elif choice == 4:
                print("Program Closed")
                break
            else:
                print("Invalid choice")

        except:
            print("Please enter numbers only")
           
info()