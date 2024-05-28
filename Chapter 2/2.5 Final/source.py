from zoo.animal import Animal
from zoo.dog import Dog
from zoo.cat import Cat
from zoo.skunk import Skunk
from zoo.unicorn import Unicorn
from zoo.dragon import Dragon


def main():
    # create the instances of the animals
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky")
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
     # create the instances of the animals, with a different hunger level
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)

    # create a list of the animals in the zoo
    zoo_lst = [dog, cat, skunk, unicorn, dragon, dog2, cat2, skunk2, unicorn2, dragon2]

    # iterate over the list of animals in the zoo and feed them
    for animal in zoo_lst:
        # if the animal is hungry, print the animal
        if animal.is_hungry():
            print(animal)
       # feed the animal until it is not hungry
        while animal.is_hungry():
            animal.feed()
        # call the talk method of each animal
        animal.talk()

        # check the type of the animal and call the appropriate method
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    # print the zoo name 'The Python Zoo' using the class attribute zoo_name
    print(Animal.zoo_name)

if __name__ == "__main__":
    main()