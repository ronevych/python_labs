"""
Module that imports AnimalHome
"""
from animal_home import AnimalHome


class Farm(AnimalHome):
    """
    Farm class represents a farm.

    It inherits from the AnimalHome class.

    Attributes:
        name (str): The name of the farm.
        location (str): The location of the farm.
        area (float): The area of the farm.
        capacity (int): The capacity of the farm.
        working_hours (int): The working hours of the farm.
        animal_carry_cost (float): The cost of carrying animals in the farm.
        animal_type (str): The type of animals in the farm.
        animal_carry_cost_per_day (float): The cost of carrying animals per day in the farm.

    Methods:
        __init__(name, location, area, capacity, working_hours, animal_carry_cost, animal_type,
                 animal_carry_cost_per_day): Initializes an instance of Farm.
        calculate_animal_carry_cost_per_month(): Calculates the animal carry cost per month.
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name, location, area, capacity, working_hours, animal_carry_cost,
                 animal_type, animal_carry_cost_per_day):
        """
        Initializes an instance of Farm.

        Args:
            name (str): The name of the farm.
            location (str): The location of the farm.
            area (float): The area of the farm.
            capacity (int): The capacity of the farm.
            working_hours (int): The working hours of the farm.
            animal_carry_cost (float): The cost of carrying animals in the farm.
            animal_type (str): The type of animals in the farm.
            animal_carry_cost_per_day (float): The cost of carrying animals per day in the farm.
        """
        super().__init__(name, location, area)
        self.capacity = capacity
        self.working_hours = working_hours
        self.animal_carry_cost = animal_carry_cost
        self.animal_type = animal_type
        self.animal_carry_cost_per_day = animal_carry_cost_per_day

    def calculate_animal_carry_cost_per_month(self):
        """
        Calculates the animal carry cost per month.

        Returns:
            float: The animal carry cost per month.
        """
        return self.animal_carry_cost_per_day * 30

    def __str__(self):
        """
        Returns a string representation of the Farm object.

        Returns:
            str: The string representation of the Farm object.
        """
        return f"Farm(name={self.name}, location={self.location}, area={self.area}, " \
               f"capacity={self.capacity}, working_hours={self.working_hours}, " \
               f"animal_carry_cost={self.animal_carry_cost}, animal_type={self.animal_type}, " \
               f"animal_carry_cost_per_day={self.animal_carry_cost_per_day})"
