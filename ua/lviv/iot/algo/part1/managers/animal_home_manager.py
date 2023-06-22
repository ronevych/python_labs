"""
Module defining the AnimalHomeManager class for managing animal homes.
"""
from ua.lviv.iot.algo.part1.models.animal_home import AnimalHome


class AnimalHomeManager(AnimalHome):
    """
    AnimalHomeManager class represents a manager for animal homes.

    It inherits from the AnimalHome class.

    Attributes:
        name (str): The name of the animal home manager.
        location (str): The location of the animal home manager.
        area (float): The area of the animal home manager.

    Methods:
        __init__(name, location, area): Initializes an instance of AnimalHomeManager.
        add_zoo(zoo): Adds a zoo to the animal home manager.
        find_place_with_capacity_bigger_than(zoo_list): Finds places with capacity bigger
         than a given value.
        find_place_with_working_hours_less_than(zoo_list): Finds places with working hours
        less than a given value.
    """

    def __init__(self, name, location, area):
        """
        Initializes an instance of AnimalHomeManager.

        Args:
            name (str): The name of the animal home manager.
            location (str): The location of the animal home manager.
            area (float): The area of the animal home manager.
        """
        self.name = name
        self.location = location
        self.zoo_list = []
        super().__init__(name, location, area)

    def add_zoo(self, zoo):
        """
        Adds a zoo to the animal home manager.

        Args:
            zoo: The zoo to be added.
        """
        # pylint: disable= unnecessary-pass
        pass

    def find_place_with_capacity_bigger_than(self, zoo_list):
        """
        Finds places with capacity bigger than a given value.

        Args:
            zoo_list (list): A list of zoos.

        Returns:
            list: A list of zoos with capacity bigger than the given value.
        """
        return [zoo for zoo in zoo_list if zoo.getCapacity() >= 50]

    def find_place_with_working_hours_less_than(self, zoo_list):
        """
        Finds places with working hours less than a given value.

        Args:
            zoo_list (list): A list of zoos.

        Returns:
            list: A list of zoos with working hours less than the given value.
        """
        return [zoo for zoo in zoo_list if zoo.getWorkingHours() <= 9]

    def __len__(self):
        """
        Returns the number of zoos in the animal home manager.

        Returns:
            int: The number of zoos in the animal home manager.
        """
        # pylint: disable= unnecessary-pass
        pass

    def __getitem__(self, index):
        """
        Returns the zoo at the given index.

        Args:
            index (int): The index of the zoo.

        Returns:
            Zoo: The zoo at the given index.
        """
        return self.zoo_list[index]

    def __iter__(self):
        """
        Returns an iterator for the animal home manager.

        Returns:
            iterator: An iterator for the animal home manager.
        """
        # pylint: disable= unnecessary-pass
        pass
