import json
import os

def add_item():

    if not os.path.exists("app/dashboard/menu.json"):
        print("Menu file not found!")
        return

    with open("app/dashboard/menu.json", "r") as file:
        menu = json.load(file)

    category = input("Enter category: ").title()
    name = input("Enter dish name: ").lower().title()

    try:
        price = int(input("Enter price: "))
    except:
        print("Invalid price")
        return

    new_dish = {
        "dish": name,
        "price": price
    }

    if category in menu:
        menu[category].append(new_dish)

        with open("app/dashboard/menu.json", "w") as file:
            json.dump(menu, file, indent=4)

        print("Dish added successfully")

    else:
        print("Category not found")
