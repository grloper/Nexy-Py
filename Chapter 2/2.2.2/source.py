class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


# Main program
animal1 = Animal("Octavio", 5)
animal2 = Animal("Octavio", 3)

animal1.birthday()

print(f"Animal 1 age: {animal1.get_age()}")
print(f"Animal 2 age: {animal2.get_age()}")