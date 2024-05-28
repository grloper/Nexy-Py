from .animal import Animal

class Skunk(Animal):
    """Class representing a skunk animal."""

    def __init__(self, name_, hunger_=0, stink_count_=6):
        super().__init__(name_, hunger_)
        self.stink_count_ = stink_count_

    def talk(self):
        print("tssssss")

    def stink(self):
        print("Dear lord!")
