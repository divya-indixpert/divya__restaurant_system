import json
import os

file_name = "table.json"

def table_booking():
    if not os.path.exists(file_name):
        tables = [{"table_no": i, "status": "Available"} for i in range(1, 41)]
        with open(file_name , "w")as file:
            json.dump(tables, file, indent=4)
            
        with open (file_name , "r") as file:
            table = json.load(file)

        print("\n===== TABLE STATUS =====")
    for t in tables:
        if t["status"] == "Booked":
            print(f"Table {t['table_no']} : Booked ({t.get('customer_name','')})")
        else:
            print(f"Table {t['table_no']} : Available")
            
    table_number = int("please enter table number you want to booked")
    for t in table:
        if t["table_no"] == table_number:

            if t["status"] == "Booked":
                print(" Table already booked")
                return
            else:
                print("invalid table number")
        
        name = 
    
    
            
            

            



