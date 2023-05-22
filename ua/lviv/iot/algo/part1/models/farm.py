from zoo import Zoo

class Farm(Zoo):
    def __init__(self, name, location, area, capacity, working_hours, animal_carry_cost, animal_type, animal_carry_cost_per_day):
        super().__init__(name, location, area, capacity, working_hours, animal_carry_cost)
        self.animal_type = animal_type
        self.animal_carry_cost_per_day = animal_carry_cost_per_day
        
    def calculate_animal_carry_cost_per_month(self):
        return self.animal_carry_cost_per_day * 30  

    def __str__(self):
        return f"Farm(name = {self.name}, location = {self.location}, area = {self.area}, capacity = {self.capacity}, working_hours = {self.working_hours}, animal_carry_cost = {self.animal_carry_cost}, animal_type = {self.animal_type}, animal_carry_cost_per_day = {self.animal_carry_cost_per_day})"