import json
import os
from app.table_booking.table import restaurant_tables

FILE = "app/dashboard/booking.json"

def table_book():
    tables = restaurant_tables()

    
    try:
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                bookings = json.load(f)
        else:
            bookings = []
    except Exception as e:
        print("File error:", e)
        bookings = []
    
    booked_tables = [b["table_no"] for b in bookings]

    print("\nTables:")
    for t in tables:
        if t["table_no"] in booked_tables:
            print(f"Table {t['table_no']} - Booked")
        else:
            print(f"Table {t['table_no']} - Available")

    try:
        table_no = int(input("Enter table number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if table_no < 1 or table_no > 10:
        print("Invalid table number! (1-10 allowed)")
        return

    if table_no in booked_tables:
        print("Table already booked!")
        return
        
    name = input("Enter name: ")
    if not name.isalpha():
        print("only alphabets (A-Z) allowed")
        return
    

    bookings.append({
        "table_no": table_no,
        "name": name
    })

  
    try:
        with open(FILE, "w") as f:
            json.dump(bookings, f, indent=4)
        print("Table booked successfully ")
    except Exception as e:
        print("Error saving booking:", e)