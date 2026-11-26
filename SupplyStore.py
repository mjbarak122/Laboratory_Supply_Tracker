import json
from SupplyItem import SupplyItem

class SupplyStore: #second class

    def __init__(self):
        self.inventory={} #creates an empty dictionary for later
        
    def add_item(self, item): #method that allows to add items 
        if item.item_id in self.inventory:
            return False
        else:
            self.inventory[item.item_id]=item #stores the object inside the dictionary 
            return True
    def search_item(self, item_id): #checks if the id exists or not
        if item_id in self.inventory:
            return self.inventory[item_id]
        else:
            return None
        
    def search_by_location(self, location):
        results = []
        for item in self.inventory.values():
            if location in item.quantities:
                results.append(item)
        return results
        
    def receive_stock(self, item_id, location, quantity): 
        #add quantity to stock as if we got supplies 
        item=self.search_item(item_id) #calls the method search item
        if item is None:
            return #checks if the item exists 
        if quantity<0:
            return #checks that the item quantity is not negative 
        if location not in item.quantities :
            return #checks if the location is valid 
        item.quantities[location]+=quantity
        return True #add the amount together 
    
    def issue_stock(self, item_id, location, quantity):
        #removes quantity from stock as if we took the supplies to use them
        item=self.search_item(item_id) #calls the method search item
        if item is None:
            return #checks if the item exists 
        if quantity<0:
            return #checks that the item quantity is not negative 
        if location not in item.quantities :
            return #checks if the location is valid 
        if quantity > item.quantities[location]:
            return
        item.quantities[location]-=quantity
        return True #subtracts the amount 
    
    def transfer_stock(self, item_id, source_location, destination_location, quantity):
        #method that allows transfering quantity from one location to another
        item=self.search_item(item_id)
        if item is None:
            return #checks if the item exists 
        if quantity<0:
            return #checks that the item quantity is not negative 
        if source_location not in item.quantities:
            return #checks if location A exisits
        if destination_location not in item.quantities:
            return #checks if location B exists 
        if source_location == destination_location:
            return #checks that the location are different 
        if quantity> item.quantities[source_location]:
            return #chekcs if the amount to transfer is greater than the stock we have
        item.quantities[source_location]-=quantity
        item.quantities[destination_location]+=quantity
        #These 2 lines do the calculation by subtracting from the source and adding to the destination
        return True 
    
    def generate_report(self, location): #method that generates report to a location
        total_cost=0 #initial total cost value
        for item in self.inventory.values(): #loops through Supplyitem
                    needed= item.below_minimum(location)
                    if needed is not None and needed>0:
                        cost=item.unit_cost*needed #calculates the cost
                        total_cost+=cost #totla cost of everything
                        print(item.item_name, needed, cost)
        print("Total Cost=", total_cost)
        
    def save_data(self,filename): #method that saves inventory to a file
        data=[] #empty list to store the item dictionaries 
        for item in self.inventory.values(): #loops through every item in inventory 
            item_data={} #empty dictionary 
            item_data["item_id"] = item.item_id
            item_data["item_name"] = item.item_name
            item_data["unit_cost"] = item.unit_cost
            item_data["min_stock"] = item.min_stock
            item_data["quantities"] = item.quantities
            #the line above copy the specified into the dictioanry
            data.append(item_data) #adds the completed dictionary to the list
        with open(filename, "w") as file: #opens file in write mode
            json.dump(data, file) #converts to json 
        print("Data saved successfully!")
        
    def load_data(self, filename): #method to load saved inventory data
        try:
            with open(filename, "r") as file: #open file in read mode
                data=json.load(file) #reads the json file and stores contents in data
            for item_data in data: #loops through every dictionary in the list
                item=SupplyItem(
                    item_data["item_id"],
                    item_data["item_name"],
                    item_data["unit_cost"],
                    item_data["min_stock"],
                    item_data["quantities"])
                #lines above retrieves stuff
                self.add_item(item) #adds the new object to inventory 
            print("Data loaded successfully (:")
                
        except FileNotFoundError: #if file not found 
            print("File not found ):")