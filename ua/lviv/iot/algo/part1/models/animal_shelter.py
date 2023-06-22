"""
Module that imports AnimalHome
"""
from animal_home import AnimalHome


class AnimalShelter(AnimalHome):
    """
    AnimalShelter class represents an animal shelter.

    Attributes:
        name (str): The name of the animal shelter.
        location (str): The location of the animal shelter.
        area (float): The area of the animal shelter.

    Methods:
        __init__(name, location, area): Initializes an instance of AnimalShelter.
        add_animal(animal): Adds an animal to the animal shelter.
    """

    def __init__(self, name, location, area, capacity):
        """
        Initializes an instance of AnimalShelter.

        Args:
            name (str): The name of the animal shelter.
            location (str): The location of the animal shelter.
            area (float): The area of the animal shelter.
        """
        self.name = name
        self.location = location
        self.area = area
        self.capacity = capacity
        super().__init__(name, location, area)

    def add_animal(self, animal):
        """
        Adds an animal to the animal shelter.

        Args:
            animal: The animal to be added.
        """

    def animal_count(self):
        """
        Returns the number of animals in the animal shelter.

        Returns:
            int: The number of animals in the animal shelter.
        """
