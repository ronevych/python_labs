from aquarium import Aquarium
from zoo import Zoo
from animal_shelter import AnimalShelter
from ua.lviv.iot.algo.part1.decorators.my_logging import logged
from ua.lviv.iot.algo.part1.exceptions.full_zoo_exception import FullZooCapacity
from animal_home import AnimalHome

if __name__ == '__main__':
    zoo1 = Zoo("Zolochiv", "Zolochiv", 50000.0, 450)
    zoo2 = Zoo("Medenychi", "Lviv", 50000.0, 700)
    zoo3 = Zoo("lololo", "bila tserkva", 50000.0, 500)

    animalShelter1 = AnimalShelter("Kyiv", "Kyiv", 30000.50, 700)
    animalShelter2 = AnimalShelter("Lviv", "Kyiv", 18000.50, 500)

    aquarium1 = Aquarium("Lviv", "Lviv", 150000.50, 500)
    aquarium2 = Aquarium("Kyiv", "Kyiv", 190000.75, 700)

    zoo_list = [zoo1, zoo2, zoo3]
    animal_shelter_list = [animalShelter1, animalShelter2]
    aquarium_list = [aquarium1, aquarium2]
    zoo_list2 = ['Kyiv`skyy', 'Medenyc`kyi', 'Odes`kyi']

    result = [str(index) + ': ' + item for index, item in enumerate(zoo_list2)]
    print(result)

    for zoo in zoo_list:
        print(f"Animal capacity in zoo is: {zoo.capacity}. Working hours of {zoo.working_hours}.")
        """
        print information about each zoo.
        """

    for animalShelter in animal_shelter_list:
        print(f"Animal capacity in animal shelter is: {animalShelter.capacity}. Located in {animalShelter.location}.")

    for aquarium in aquarium_list:
        print(f"Animal capacity in aquarium is: {aquarium.capacity}. and named {aquarium.name}.")


    @logged(FullZooCapacity, mode="console")
    def check_capacity(capacity):
        if capacity > 700 or capacity < 0:
            raise FullZooCapacity("The zoo has reached its maximum capacity!")


    check_capacity(800)


    obj1 = AnimalHome('Jojo', 'Berlin', 1000)
    obj2 = AnimalHome('Mamba', 'London', 1200)
    obj3 = AnimalHome('Tronik', 'Barcelona', 1500)

    manager_list = [obj1, obj2, obj3]

    result_list = [obj.do_something() for obj in manager_list]
    print(result_list)

    def get_attribute_by_type(obj, data_type):
        return{key: value for key, value in obj.__dict__.items() if isinstance(value, data_type)}

    my_object = AnimalHome('Jojo', 'Berlin', 1000)

    int_attributes = get_attribute_by_type(my_object, int)
    print(int_attributes)

    str_attributes = get_attribute_by_type(my_object, str)
    print(str_attributes)


    def check_condition(manager_list, condition):
        result = {
            'all': all(condition(obj) for obj in manager_list),
            'any': any(condition(obj) for obj in manager_list)
        }
        return result


    def condition(obj):
        return obj.area > 1000

    manager_list = [obj1, obj2, obj3]

    result = check_condition(manager_list, condition)
    print(result)

