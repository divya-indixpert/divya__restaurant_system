import json
import os
from  app.table_booking.table import restaurant_tables

FILE = "app/dashboard/booking.json"

def table_book():
    tables = restaurant_tables()
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            bookings = json.load(f)
    else:
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
        print("invalid output")
        return
    
    if table_no < 1 or table_no > 10:
        print("invalid table numbers")
        return
    
    if table_no in booked_tables:
        print("Already booked ")
        return

    name = input("Enter name: ")

    bookings.append({
        "table_no": table_no,
        "name": name
    })

    with open(FILE, "w") as f:
        json.dump(bookings, f, indent=4)

    print("Table booked successfully ")