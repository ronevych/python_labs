import abc

class AnimalHome(abc.ABC):
    
    def __init__(self, name, location, area):
        self.   name = name
        self.location = location
        self.area = area
        
    def __str__(self):
        return f"AnimalHome(name = {self.name}, location = {self.location}, area = {self.area})"