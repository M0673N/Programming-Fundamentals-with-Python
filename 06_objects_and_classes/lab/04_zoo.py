class Zoo:
    __animals = []
    mammals = []
    fishes = []
    birds = []

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals.append(name)

    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}")
        elif species == "fish":
            print(f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}")
        elif species == "bird":
            print(f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}")
        print(f"Total animals: {len(self.__animals)}")


zoo = Zoo(input())

n = int(input())
for i in range(n):
    animal = input()
    species, name = animal.split()
    zoo.add_animal(species, name)

zoo.get_info(input())
