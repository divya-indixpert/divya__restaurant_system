from app.menu.item import show_menu
from app.menu.add_new_dish import add_item
from app.menu.update import update_item
from app.menu.delete import delete_item

print("\nWelcome to Restaurant Management System 🍽️")
def admin_menu():
    
    while True:

        print("\n===================================")
        print("        🍽️  RESTAURANT MENU 🍽️      ")
        print("===================================")
        print("1️⃣ View Items")
        print("2️⃣ Add New Item")
        print("3️⃣ Update Item")
        print("4️⃣ Delete Item")
        print("5️⃣ Exit")
        print("===================================")

        
        choice = int(input("Enter your choice:"))

        if choice == 1:
            print("\nShowing Menu...")
            show_menu()

        elif choice == 2:
            print("\nAdd New Dish")
            add_item()

        elif choice == 3:
            print("\nUpdate Dish")
            update_item()

        elif choice == 4:
            print("\nDelete Dish")
            delete_item()

        elif choice == 5:
            print("\nThank you for using the system! ")
            break

        else:
            print("Invalid choice, try again")