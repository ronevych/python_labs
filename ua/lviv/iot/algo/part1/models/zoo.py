from animal_home import AnimalHome

class Zoo(AnimalHome):
    
    __instance = None
    
    def __init__(self, name = "", location = "", area = 0, capacity = 0, working_hours = 8, animal_carry_cost = 0):
        super().__init__(name, location, area)
        self.capacity = capacity
        self.working_hours = working_hours
        self.animal_carry_cost = animal_carry_cost
        

    def increase_capacity(self, new_capacity):
        self.capacity += new_capacity
        
    def split_area(self):
        self.area /= 2
        
    def add_new_region(self, new_area):
        self.area += new_area
        
    def __str__(self):
        return (f"Zoo(name : {self.name}, location : {self.location}, area : "
                f"{self.area}, capacity : {self.capacity})") 
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Zoo("Kyivs`kyy", "Kyiv", 2000, 700)
            return cls.__instance
        
if __name__ == '__main__':
    zoo1 = Zoo("Lvivs`kyy", "Lviv", 1000, 500)
    zoo2 = Zoo()
    zoo_list = [zoo1, zoo2, Zoo.get_instance()]
    for i in zoo_list:
            print(i)
        
    

