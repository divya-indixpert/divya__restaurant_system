from app.table_booking.booking import table_book
from app.table_booking.cancel import cancel_booking

def menu():
    try:
        while True:
            print("\n===== TABLE BOOKING =====")
            print("1. Book Table")
            print("2. Cancel Booking")
            print("3. Exit")
            
            
            choice = input("Enter choice: ")

            if choice == "1":
                table_book()

            elif choice == "2":
                cancel_booking()

            elif choice == "3":
                exit
                break

            else:
                print("Invalid choice")
                    
    except Exception as e:
        print(e)
            
                


                

            
