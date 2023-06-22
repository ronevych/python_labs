"""
Modules of full_zoo_exception, ua.lviv.iot.algo.part1.models.animal_home,
ua.lviv.iot.algo.part1.decorators.my_logging
"""
# pylint: disable=import-error
from ua.lviv.iot.algo.part1.exceptions.full_zoo_exception import FullZooCapacity
from ua.lviv.iot.algo.part1.models.animal_home import AnimalHome
from ua.lviv.iot.algo.part1.decorators.my_logging import logged


class Zoo(AnimalHome):
    """
    Zoo class represents a zoo.

    It inherits from the AnimalHome class.

    Attributes:
        name (str): The name of the zoo.
        location (str): The location of the zoo.
        area (float): The area of the zoo.
        capacity (int): The capacity of the zoo.
        working_hours (int): The working hours of the zoo.
        animal_carry_cost (float): The cost of carrying animals in the zoo.

    Methods:
        __init__(name="", location="", area=0, capacity=0, working_hours=8, animal_carry_cost=0):
            Initializes an instance of Zoo.
        increase_capacity(new_capacity): Increases the capacity of the zoo.
        split_area(): Splits the area of the zoo.
        add_new_region(new_area): Adds a new region to the zoo.
        __str__(): Returns a string representation of the Zoo object.
        get_instance(): Returns a singleton instance of the Zoo class.
    """

    __instance = None

    # pylint: disable=line-too-long
    # pylint: disable= too-many-arguments
    def __init__(self, name="", location="", area=0, capacity=0, working_hours=8, animal_carry_cost=0):
        """
        Initializes an instance of Zoo.

        Args:
            name (str): The name of the zoo. (default: "")
            location (str): The location of the zoo. (default: "")
            area (float): The area of the zoo. (default: 0)
            capacity (int): The capacity of the zoo. (default: 0)
            working_hours (int): The working hours of the zoo. (default: 8)
            animal_carry_cost (float): The cost of carrying animals in the zoo. (default: 0)
        """
        super().__init__(name, location, area)
        self.working_hours = working_hours
        self.animal_carry_cost = animal_carry_cost
        self.check_capacity(capacity)

    def increase_capacity(self, new_capacity):
        """
        Increases the capacity of the zoo.

        Args:
            new_capacity (int): The additional capacity to be added to the zoo.
        """
        self.capacity += new_capacity

    def split_area(self):
        """
        Splits the area of the zoo.
        """
        # pylint: disable=no-member
        self.area /= 2

    def add_new_region(self, new_area):
        """
        Adds a new region to the zoo.

        Args:
            new_area (float): The area of the new region to be added to the zoo.
        """
        # pylint: disable=no-member
        self.area += new_area

    def __str__(self):
        """
        Returns a string representation of the Zoo object.

        Returns:
            str: The string representation of the Zoo object.
        """
        # pylint: disable=line-too-long
        # pylint: disable=no-member
        return f"Zoo(name: {self.name}, location: {self.location}, area: {self.area}, capacity: {self.capacity})"

    @classmethod
    def get_instance(cls):
        """
        Returns a singleton instance of the Zoo class.

        Returns:
            Zoo: The singleton instance of the Zoo class.
        """
        if not cls.__instance:
            cls.__instance = Zoo("Kyivs'kyy", "Kyiv", 2000, 700)
        return cls.__instance

    @logged(FullZooCapacity, mode="console")
    def check_capacity(self, capacity):
        """
        Method that checks capacity of zoo and raise an exception if capacity is over 700
        """
        if capacity > 700 or capacity < 0:
            raise FullZooCapacity("The zoo has reached it max capacity!")
        self.capacity = capacity