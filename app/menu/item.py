import json
import os

def food_menu():
    menu_items = {
        "Breakfast": [
            {"dish": "Masala Dosa", "price": 110},
            {"dish": "Plain Dosa", "price": 90},
            {"dish": "Idli Sambar", "price": 80},
            {"dish": "Vada Sambar", "price": 90},
            {"dish": "Aloo Paratha", "price": 80},
            {"dish": "Gobi Paratha", "price": 90},
            {"dish": "Paneer Paratha", "price": 100},
            {"dish": "Upma", "price": 70},
            {"dish": "Poha", "price": 60},
            {"dish": "Bread Omelette", "price": 80}
        ],

        "Lunch": [
            {"dish": "Paneer Butter Masala", "half": 150, "full": 250},
            {"dish": "Shahi Paneer", "half": 140, "full": 240},
            {"dish": "Dal Makhani", "half": 120, "full": 200},
            {"dish": "Rajma Chawal", "half": 80, "full": 130},
            {"dish": "Chole Bhature", "half": 70, "full": 120},
            {"dish": "Veg Biryani", "half": 120, "full": 180},
            {"dish": "Kadai Paneer", "half": 150, "full": 240},
            {"dish": "Mix Veg", "half": 110, "full": 180},
            {"dish": "Aloo Jeera", "half": 90, "full": 150},
            {"dish": "Palak Paneer", "half": 140, "full": 230}
        ],

        "Dinner": [
            {"dish": "Butter Chicken", "half": 180, "full": 280},
            {"dish": "Chicken Curry", "half": 150, "full": 230},
            {"dish": "Fish Curry", "half": 170, "full": 270},
            {"dish": "Prawn Masala", "half": 200, "full": 320},
            {"dish": "Egg Curry", "half": 100, "full": 150},
            {"dish": "Chicken Biryani", "half": 150, "full": 220},
            {"dish": "Mutton Biryani", "half": 200, "full": 300},
            {"dish": "Tandoori Chicken", "half": 170, "full": 260},
            {"dish": "Chicken Korma", "half": 180, "full": 270},
            {"dish": "Mutton Curry", "half": 210, "full": 310}
        ],

        "Fast Food": [
            {"dish": "Burger", "price": 120},
            {"dish": "Cheese Burger", "price": 150},
            {"dish": "French Fries", "price": 100},
            {"dish": "Sandwich", "price": 90},
            {"dish": "Grilled Sandwich", "price": 110},
            {"dish": "Veg Pizza", "price": 220},
            {"dish": "Chicken Pizza", "price": 260},
            {"dish": "Spring Roll", "price": 120},
            {"dish": "Noodles", "price": 140},
            {"dish": "Fried Rice", "price": 150}
        ],

        "Sweets": [
            {"dish": "Gulab Jamun", "price": 60},
            {"dish": "Rasgulla", "price": 60},
            {"dish": "Jalebi", "price": 70},
            {"dish": "Kheer", "price": 90},
            {"dish": "Ice Cream", "price": 80},
            {"dish": "Chocolate Cake", "price": 120},
            {"dish": "Brownie", "price": 110},
            {"dish": "Fruit Custard", "price": 100},
            {"dish": "Laddu", "price": 50},
            {"dish": "Barfi", "price": 70}
        ]
    }

    return menu_items

from colorama import Fore, Style, init
init(autoreset=True)

def show_menu():

    if not os.path.exists("app/dashboard/menu.json"):
        with open("menu.json", "w") as file:
            json.dump(food_menu(), file, indent=4)

    with open("app/dashboard/menu.json", "r") as file:
        menu = json.load(file)

    print(Fore.CYAN + Style.BRIGHT + "\n" + "═"*60)
    print(Fore.YELLOW + Style.BRIGHT + "         ✨ THE ROYAL PLATE MENU ✨".center(60))
    print(Fore.CYAN + "═"*60)

    item_no = 1

    for category, items in menu.items():

        print(Fore.MAGENTA + "\n" + "─"*60)
        print(Fore.GREEN + Style.BRIGHT + f" {category.upper()} ".center(60, " "))
        print(Fore.MAGENTA + "─"*60)

        for item in items:

            if "price" in item:
                print(
                    Fore.WHITE +
                    f"{item_no:2}. {item['dish']:<30}" +
                    Fore.YELLOW + f" ₹ {item['price']:>5}"
                )
            else:
                print(
                    Fore.WHITE +
                    f"{item_no:2}. {item['dish']:<30}" +
                    Fore.CYAN + f" Half ₹{item['half']} | Full ₹{item['full']}"
                )

            item_no += 1

    print(Fore.CYAN + "\n" + "═"*60)