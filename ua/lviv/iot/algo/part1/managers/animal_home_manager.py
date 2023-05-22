from farm import Farm

class AnimalHomeManager (Farm):
    def addZoo(self, zoo):
        pass

    def findPlaceWithCapacityBiggerThan(self, zooList):
        return [zoo for zoo in zooList if zoo.getCapacity() >= 50]

    def findPlaceWithWorkingHoursLessThan(self, zooList):
        return [zoo for zoo in zooList if zoo.getWorkingHours() <= 9]


class Zoo:
    def __init__(self, capacity, workingHours, animalCarryCost):
        self.capacity = capacity
        self.workingHours = workingHours
        self.animalCarryCost = animalCarryCost


class AnimalShelter:
    def __init__(self, capacity, workingHours, animalCarryCost):
        self.capacity = capacity
        self.workingHours = workingHours
        self.animalCarryCost = animalCarryCost


class Aquarium:
    def __init__(self, capacity, workingHours, animalCarryCost):
        self.capacity = capacity
        self.workingHours = workingHours
        self.animalCarryCost = animalCarryCost


if __name__ == '__main__':
    zoo1 = Zoo(50, 8, 50000.0)
    zoo2 = Zoo(70, 10, 50000.0)

    animalShelter1 = AnimalShelter(150, 8, 30000.50)
    animalShelter2 = AnimalShelter(100, 8, 18000.50)

    aquarium1 = Aquarium(550, 8, 150000.50)
    aquarium2 = Aquarium(675, 8, 190000.75)

    zooList = [zoo1, zoo2]
    animalShelterList = [animalShelter1, animalShelter2]
    aquariumList = [aquarium1, aquarium2]

    for zoo in zooList:
        print(f"Animal capacity in zoo is: {zoo.capacity}. Working hours of {zoo.workingHours}. Animal cost: {zoo.animalCarryCost}")

    for animalShelter in animalShelterList:
        print(f"Animal capacity in animal shelter is: {animalShelter.capacity}. Working hours of {animalShelter.workingHours}. Animal cost: {animalShelter.animalCarryCost}")

    for aquarium in aquariumList:
        print(f"Animal capacity in aquarium is: {aquarium.capacity}. Working hours of {aquarium.workingHours}. Animal cost: {aquarium.animalCarryCost}")
