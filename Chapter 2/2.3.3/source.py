class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        Octopus.count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


# Create two instances of Octopus
octopus1 = Octopus("Octopus1")
octopus2 = Octopus()

# Print the names of the instances
print(octopus1.get_name())
print(octopus2.get_name())

# Change the name of one instance
octopus1.set_name("New Octopus1")

# Print the new name
print(octopus1.get_name())

# Print the count of animals
print(Octopus.count_animals)