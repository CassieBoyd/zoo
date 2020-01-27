class Habitat:

    def __init__(self, name):
        self.name = name
        # Empty set to be filled with instances
        self.animals = set()

    def add_animal(self, animal):
        self.animals.add(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)
# String
    def __str__(self):
        return f'{self.name} ({len(self)} animals)'
# Length
    def __len__(self):
        return len(self.animals)