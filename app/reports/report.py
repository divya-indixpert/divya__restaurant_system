import json
import os
from collections import defaultdict

BILL_FILE = "app/dashboard/bill.json"
BOOKING_FILE = "app/dashboard/booking.json"

def sales_report():

   
    if not os.path.exists(BILL_FILE):
        print("No billing data found!")
        return

    try:
        with open(BILL_FILE, "r") as f:
            data = json.load(f)
    except Exception as e:
        print("Error reading bill file:", e)
        return

   
    try:
        if os.path.exists(BOOKING_FILE):
            with open(BOOKING_FILE, "r") as f:
                bookings = json.load(f)
        else:
            bookings = []
    except Exception as e:
        print("Error reading booking file:", e)
        bookings = []

    total_customers = len(bookings)   

    item_count = defaultdict(int)
    total_revenue = 0

    for bill in data:
        items = bill.get("items", [])

        for item in items:
            if isinstance(item, dict):
                name = item.get("name")
                qty = item.get("quantity", 1)
                price = item.get("price", 0)

                item_count[name] += qty
                total_revenue += price * qty

    if not item_count:
        print("No valid sales data available")
        return

    print("\n SALES REPORT")
    print("="*40)

    for item, qty in item_count.items():
        print(f"{item} ➜ {qty} sold")

   
    highest_item = max(item_count, key=item_count.get)
    print(f"\n Highest Selling Item: {highest_item} ({item_count[highest_item]} sold)")

    # 💰 Revenue
    print(f"\n Total Revenue: ₹{total_revenue}")

 
    print(f"\n Total Customers (Table Booking): {total_customers}")