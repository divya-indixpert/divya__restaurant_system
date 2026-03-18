import json
def update_item():

    with open("menu.json", "r") as file:
        menu = json.load(file)

    name = input("Enter dish name to update price: ")

    for category, items in menu.items():

        for item in items:

            if item["dish"].lower() == name.lower():

                if "price" in item:
                    new_price = int(input("Enter new price: "))
                    item["price"] = new_price

                else:
                    half = int(input("Enter new half price: "))
                    full = int(input("Enter new full price: "))
                    item["half"] = half
                    item["full"] = full

                with open("menu.json", "w") as file:
                    json.dump(menu, file, indent=4)

                print("Price updated successfully ")
                return

    print("Dish not found ")