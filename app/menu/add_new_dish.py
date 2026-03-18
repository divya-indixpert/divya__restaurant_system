import json
import os

def add_item():

    if not os.path.exists("menu.json"):
        print("Menu file not found!")
        return

    with open("menu.json", "r") as file:
        menu = json.load(file)

    category = input("Enter category: ")
    name = input("Enter dish name: ")

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

        with open("menu.json", "w") as file:
            json.dump(menu, file, indent=4)

        print("Dish added successfully")

    else:
        print("Category not found")
