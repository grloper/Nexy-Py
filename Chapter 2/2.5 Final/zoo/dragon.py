from .animal import Animal

class Dragon(Animal):
    """Class representing a dragon animal."""

    def __init__(self, name_, hunger_=0, color_="Green"):
        super().__init__(name_, hunger_)
        self.color_ = color_

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")
