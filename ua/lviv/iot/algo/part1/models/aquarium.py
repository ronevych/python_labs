"""
Module that imports AnimalHome
"""
from animal_home import AnimalHome


class Aquarium(AnimalHome):
    """
    Aquarium class represents an aquarium.

    It inherits from the AnimalHome class.

    Attributes:
        name (str): The name of the aquarium.
        location (str): The location of the aquarium.
        area (float): The area of the aquarium.

    Methods:
        __init__(name, location, area): Initializes an instance of Aquarium.
    """

    def __init__(self, name, location, area, capacity):
        """
        Initializes an instance of Aquarium.

        Args:
            name (str): The name of the aquarium.
            location (str): The location of the aquarium.
            area (float): The area of the aquarium.
        """
        self.area = area
        self.location = location
        self.area = area
        self.capacity = capacity
        super().__init__(name, location, area)

    def add_animal(self, animal):
        """
        Adds an animal to the aquarium.

        Args:
            animal: The animal to be added.
        """


    def animal_count(self):
        """
        Returns the number of animals in the aquarium.

        Returns:
            int: The number of animals in the aquarium.
        """
