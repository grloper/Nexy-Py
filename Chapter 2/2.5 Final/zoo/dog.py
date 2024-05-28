from .animal import Animal

class Dog(Animal):
    """Class representing a dog animal."""

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")
