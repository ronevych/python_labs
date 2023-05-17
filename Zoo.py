class Zoo:
    
    instance = None
    
    def __init__(self, name = "", location = "", area = 0, capacity = 0):
        self.name = name
        self.location = location
        self.area = area
        self.capacity = capacity

    def increase_capacity(self, new_capacity):
        self.capacity += new_capacity
        
    def split_area(self):
        self.area /= 2
        
    def add_new_region(self, new_area):
        self.area += new_area
        
    def __str__(self):
        return (f"Zoo(name : {self.name}, location : {self.location}, area : "
                f"{self.area}, capacity : {self.capacity})") 
    
    @staticmethod
    def get_instance():
        Zoo.instance = Zoo()
        return Zoo.instance
    
zoo1 = Zoo("Lvivs`kyy", "Lviv", 1000, 500)
zoo2 = Zoo()
zoo_list = [zoo1, zoo2, Zoo.get_instance()]
for i in zoo_list:
    print(i)