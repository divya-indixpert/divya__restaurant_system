import datetime
import json
import os

from app.bill.customer import customer_detail
from app.bill.dish_name import food_menu
from app.bill.payment_method import payment

FILE = "app/dashboard/bill.json"

# ✅ Save bill function
def save_bill(items):
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    data.append({
        "items": items
    })

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def billing():

    print("\n========== CUSTOMER DETAILS ==========")
    customer = customer_detail()
    name = customer["name"]
    email = customer["email"]
    contact = customer["contact"]
    

    print("\n========== FOOD ORDER ==========")
    items, subtotal = food_menu()

    print("\n========== PAYMENT ==========")
    pay_method = payment()

    gst = subtotal * 0.05
    grand_total = subtotal + gst

    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # ================= FINAL BILL =================
    print("\n==========================================")
    print("            FINAL BILL")
    print("==========================================")

    print(f"Customer Name : {name}")
    print(f"Email         : {email}")
    print(f"Contact       : {contact}")
    print(f"Date & Time   : {date_time}")

    print("------------------------------------------")
    print("Dish\t\tQty\tPrice\tTotal")

    for item in items:
        print(f"{item['name']}\t{item['quantity']}\t₹{item['price']}\t₹{item['total']}")

    print("------------------------------------------")
    print(f"Subtotal      : ₹{subtotal}")
    print(f"GST (5%)      : ₹{gst:.2f}")
    print(f"Grand Total   : ₹{grand_total:.2f}")
    print(f"Payment Mode  : {pay_method}")

    print("==========================================")
    print("      THANK YOU! VISIT AGAIN ")
    print("==========================================")

    save_bill(items)