import json

def delete_item():

    with open("menu.json", "r") as file:
        menu = json.load(file)

    name = input("Enter dish name to delete: ")

    for category, items in menu.items():

        for item in items:

            if item["dish"] == name:

                items.remove(item)

                with open("menu.json", "w") as file:
                    json.dump(menu, file, indent=4)

                print("Dish deleted successfully ")
                return

    print("Dish not found ")