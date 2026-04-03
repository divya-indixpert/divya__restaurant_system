def food_menu():
    items = []
    total_bill = 0

    while True:
        while True:
            food_category = input("Enter food category (Fastfood/Sweets/Breakfast/Lunch/Dinner): ").lower()
            if food_category not in ["Fast food", "Sweets", "Breakfast", "Lunch", "Dinner"]:
                print("Invalid category! Try again.")
            else:
                break

       
        food_name = input("Enter food name: ")

        while True:
            food_price = input("Enter food price: ")
            if not food_price.isdigit():
                print("Price must be a number")
            else:
                food_price = int(food_price)
                break


        while True:
            quantity = input("Enter quantity: ")
            if not quantity.isdigit():
                print("Quantity must be a number")
            else:
                quantity = int(quantity)
                break

    
        while True:
            plate = input("Enter plate type (half/full): ").lower()
            if plate not in ["half", "full"]:
                print("Invalid plate type")
            else:
                break

    
        total = food_price * quantity
        total_bill += total
        
        items.append({
            "category": food_category,
            "name": food_name,
            "price": food_price,
            "quantity": quantity,
            "plate": plate,
            "total": total
        })

        more = input("Add more items? (yes/no): ").lower()
        if more != "yes":
            break

    return items, total_bill