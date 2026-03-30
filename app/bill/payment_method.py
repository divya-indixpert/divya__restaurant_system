def payment():

    while True:
        print("\nPayment Method")
        print("1. Cash")
        print("2. UPI")
        print("3. Card")
        
        try:
        
            p = input("Select payment method: ")

            if not p.isdigit():
                print("Please enter a valid number")
                continue

            p = int(p)

            if p == 1:
                return "Cash"
            elif p == 2:
                return "UPI"
            elif p == 3:
                return "Card"
            else:
                print("Invalid choice, try again")
                
        except Exception as e:
            print(e)