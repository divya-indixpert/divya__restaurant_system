def customer_detail():
    while True:
        name = input("Please enter your name: ")
        if not name.replace(" ", "").isalpha():
            print("Invalid name! Only alphabets allowed.")
        else:
            break


    while True:
        email = input("Please enter your email: ")
        if "@" not in email or "." not in email:
            print("Invalid email format, try again")
        else:
            break


    while True:
        contact = input("Please enter your contact number: ")
        if not contact.isdigit() or len(contact) != 10:
            print("Invalid contact number! Enter 10 digits.")
        else:
            break

    return name, email, contact