class SupplyItem: #creates class
    def __init__(self, item_id, item_name, unit_cost, min_stock, quantities):
        self.item_id=item_id
        self.item_name=item_name
        self.unit_cost=unit_cost
        self.min_stock=min_stock
        self.quantities=quantities
    #the lines above save information inside the objects
    def calculate_total_value(self):
        total_value=0
        for quantity in self.quantities.values():
            total_value+=quantity
        total_value=total_value*self.unit_cost
        return total_value
    
    def below_minimum(self, location):
        if location in self.quantities:
            needed = self.min_stock - self.quantities[location]
            if needed > 0:
                return needed
            else:
                return 0
        return None
