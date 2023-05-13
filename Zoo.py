class Zoo:
    
    def __init__(self, name, location, area, capacity):
        self.       name = name
        self.location = location
        self.area = area
        self.capacity = capacity

    def increase_capacity(self, new_capacity):
        self.capacity += new_capacity
        
    def split_area(self):
        self.area /= 2
        
    def add_new_region(self, new_area):
        self.area += new_area

