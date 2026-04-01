import json
import os
from app.table_booking.table import restaurant_tables

FILE = "app/dashboard/booking.json"

def cancel_booking():

    tables = restaurant_tables()

    try:
      
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                bookings = json.load(f)
        else:
            bookings = []

    
    except Exception as e:
        print("Error:", e)
        return

    if not bookings:
        print("No bookings found to cancel")
        return

 
    print("\nBooked Tables:")
    for b in bookings:
        print(f"Table {b['table_no']} - {b['name']}")

    try:
        table_no = int(input("Enter table number to cancel: "))
    except ValueError:
        print("Invalid input! Enter number only.")
        return

  
    for b in bookings:
        if b["table_no"] == table_no:
            bookings.remove(b)

            try:
                with open(FILE, "w") as f:
                    json.dump(bookings, f, indent=4)
                print(" Booking cancelled successfully")
            except Exception as e:
                print("Error saving file:", e)

            return

    print(" Booking not found")