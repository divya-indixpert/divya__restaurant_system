import json
import os

FILE = "app/dashboard/menu.json"

def update_item():
   
    if not os.path.exists(FILE):
        print(" Menu file not found!")
        return

    try:
        with open(FILE, "r") as file:
            menu = json.load(file)
    except json.JSONDecodeError:
        print(" File is empty or corrupted!")
        return

   
    name = input("Enter dish name to update price: ").title()
    if not name:
        print(" Dish can't be empty!")
        return

    found = False

    
    for category, items in menu.items():
        for item in items:
            if item.get("dish", "").lower() == name.lower():

               
                price_input = input("Enter new price: ").strip()
                
                if not price_input.isdigit():
                    print(" Price must be a number!")
                    return

                new_price = int(price_input)

                if new_price <= 0:
                    print(" Price must be greater than 0!")
                    return

                item["price"] = new_price
                found = True
                break

        if found:
            break

    if not found:
        print(" Dish not found!")
        return

   
    try:
        with open(FILE, "w") as file:
            json.dump(menu, file, indent=4)
        print(" Price updated successfully!")
    except Exception as e:
        print(" Error saving file:", e)