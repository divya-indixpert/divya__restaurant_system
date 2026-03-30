from app.auth.manage import details
from app.table_booking.menu_booking import menu
from app.menu.menu_items import admin_menu
from app.bill.menu import billing

def info():
    while True:

        try:
            print("\n========= The Royal Plate =========")
            print("1. User Management")
            print("2. Table Booking")
            print("3. Restaurant menu")
            print("4. billing")
            print("5. Exit")
    

            choice = int(input("Enter your choice: "))

            if choice == 1:
                details()
                  
            elif choice == 2:
                menu()

            elif choice == 3:
                admin_menu()
                
            elif choice == 4:
               billing()
                
            elif choice == 5:
                print("Program Closed")
                break
            else:
                print("Invalid choice")

        except:
            print("Please enter numbers only")
           
info()