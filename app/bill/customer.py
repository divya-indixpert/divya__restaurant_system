def customer_detail():
    while True:
        try:
            name = input("Enter your name: ").strip()
            if not name.replace(" ", "").isalpha():
                raise ValueError("Name must contain only alphabets")
            break
        except ValueError as e:
            print(f"{e}")


    while True:
        try:
            email = input("Enter your email: ").strip()
            if "@" not in email or "." not in email:
                raise ValueError("Invalid email format")
            break
        except ValueError as e:
            print(f" {e}")


    while True:
        try:
            contact = input("Enter your contact number: ").strip()
            if not contact.isdigit():
                raise ValueError("Only digits allowed")
            if len(contact) != 10:
                raise ValueError("Contact must be 10 digits")
            break
        except ValueError as e:
            print(f"{e}")

    return {
        "name": name,
        "email": email,
        "contact": contact
    }