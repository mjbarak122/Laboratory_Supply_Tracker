from SupplyItem import SupplyItem
from SupplyStore import SupplyStore
store=SupplyStore()
while True:
   print("\nLaboratory Supply Tracker")
   print("1. Add item")
   print("2. Search item")
   print("3. Receive stock")
   print("4. Issue stock")
   print("5. Transfer stock")
   print("6. Generate report")
   print("7. Save data")
   print("8. Load data")
   print("9. Exit")

   choice = input("Enter your choice: ").lower()

   match choice:
        case "1" | "add" | "a":
            item_id = int(input("Enter item ID: "))
            if item_id<=0:
                print("Item ID must be positive")
            else:
                item_name = input("Enter item name: ")
                unit_cost = float(input("Enter unit cost: "))
                if unit_cost<0:
                    print("Invalid price!")
                else:
                    min_stock = int(input("Enter minimum stock: "))
                    if min_stock<0:
                        print("Invalid stock number")
                    else:  
                        quantities = {}
                        num_locations = int(input("How many locations? "))
                        if num_locations<=0:
                            print("Invalid number of locations")
                        else:
                            valid =True
                            for i in range(num_locations):
                                location_name = input("Enter location name: ")
                                quantity = int(input("Enter quantity: "))
                                if quantity<0:
                                    print("Invalid number of quantity")
                                    valid=False
                                else:
                                    quantities[location_name] = quantity
                            if valid:
                                item = SupplyItem(item_id, item_name, unit_cost, min_stock, quantities)
                                result = store.add_item(item)
                                if result is True:
                                    print("Item added successfully")
                                else:
                                    print("Item ID already exists")   
                            else:
                                print("Item was not added because of invalid quantities")
        case "2" | "search" | "s":
            search_type = input("Search by (1) ID or (2) Location: ")

            if search_type == "1":
                item_id = int(input("Enter item ID: "))
                item = store.search_item(item_id)

                if item is not None:
                    print("Item ID:", item.item_id)
                    print("Item Name:", item.item_name)
                    print("Unit Cost:", item.unit_cost)
                    print("Minimum Stock:", item.min_stock)
                    print("Quantities:", item.quantities)
                else:
                    print("Item not found")

            elif search_type == "2":
                location = input("Enter location: ")
                results = store.search_by_location(location)
                
                if len(results) == 0:
                    print("No items found at this location")
                else:
                    for item in results:
                       print("Item ID:", item.item_id)
                       print("Item Name:", item.item_name)
                       print("Quantities:", item.quantities[location])
                
            else:
                  print("Invalid search option")
            
        case "3"|"receive"|"r":
            item_id=int(input("Enter Item ID: "))
            location=input("Enter item Location: ")
            quantity=int(input("Enter quantity received: "))
            result= store.receive_stock(item_id, location, quantity)
            if result is True:
                print("Stock received successfully")
            else: 
                print("Could not receive stock")
        case "4"|"issue"|"i":
            item_id=int(input("Enter Item ID: "))
            location=input("Enter item Location: ")
            quantity=int(input("Enter quantity needs to be issued: "))
            result=store.issue_stock(item_id, location, quantity)
            if result is True:
                print("Stock issued successfully")
            else: 
                print("Could not issue stock")
        case "5"|"transfer"|"t":
            item_id=int(input("Enter Item ID: "))
            source_location= input("Enter source location: ")
            destination_location=input("Enter destination location: ")
            quantity=int(input("Enter item quantity: "))
            result=store.transfer_stock(item_id, source_location, destination_location, quantity)
            if result is True:
                print("Stock transferred successfully")
            else: 
                print("Could not transfer stock")
        case "6"|"generate"|"g":
            location=input("Enter location of the report you want to generate: ")
            store.generate_report(location)
        case "7"|"save"|"sa":
            filename=input("Enter the name of the file you want to save: ")
            store.save_data(filename)
        case "8"|"load"|"l":
            filename=input("Enter name of the file you want to load: ")
            store.load_data(filename)
        case "9"|"exit"|"e":
            print("Thank you for using the labrotary supply tracker!")
            break
        case _:
            print("Invalid choice!")

