def customer_detail():
    
    name = input("please enter your name:")
    email = input("please enter your email: ")
    if "@" not in email:
        print("Invalid email format")
        return
        
    contact = input("please enter your contact number: ")
    if not contact.isdigit() or len(contact) != 10:
        print("Invalid contact number")
        return
    
    return name, email, contact