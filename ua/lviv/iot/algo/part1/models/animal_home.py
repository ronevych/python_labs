"""
Module defining the AnimalHome class representing an animal home.
"""

from abc import ABC, abstractmethod


class AnimalHome(ABC):
    """
    AnimalHome is an abstract base class representing an animal home.

    Attributes:
        name (str): The name of the animal home.
        location (str): The location of the animal home.
        area (float): The area of the animal home.

    Methods:
        __init__(name, location, area): Initializes an instance of AnimalHome.
        __str__(): Returns a string representation of the AnimalHome object.
        get_name(): Get the name of the object.
        find_animal(name): Find an animal in the animal home by name.
    """

    def __init__(self, name, location, area):
        """
        Initializes an instance of AnimalHome.

        Args:
            name (str): The name of the animal home.
            location (str): The location of the animal home.
            area (float): The area of the animal home.
        """
        self.name = name
        self.location = location
        self.area = area

    def __str__(self):
        """
        Returns a string representation of the AnimalHome object.

        Returns:
            str: A string representation of the AnimalHome object.
        """
        return f"AnimalHome(name={self.name}, location={self.location}, area={self.area})"

    def get_name(self):
        """
        Get the name of the object.

        Returns:
            str: The name of the object.
        """
        return self.name

    def find_animal(self, name):
        """
        Find an animal in the animal home by name.

        Args:
            name (str): The name of the animal to search for.

        Returns:
            Animal or None: The found animal object or None if not found.
        """
        # pylint: disable=unnecessary-pass
        pass

    def do_something(self):
        pass
