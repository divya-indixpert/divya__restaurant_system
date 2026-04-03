import json

def delete_item():

    FILE = "app/dashboard/menu.json"

    with open(FILE, "r") as file:
        menu = json.load(file)

    name = input("Enter dish name to delete: ")

    for category, items in menu.items():

        for item in items:

            if item["dish"].lower() == name.lower(): 
                items.remove(item)

                with open(FILE, "w") as file:         
                    json.dump(menu, file, indent=4)

                print("Dish deleted successfully ")
                return

    print("Dish not found ")