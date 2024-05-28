class Animal:
    """
    Represents an animal in a zoo.

    Attributes:
        zoo_name (str): The name of the zoo.
        _name (str): The name of the animal.
        _hunger (int): The hunger level of the animal.
    """

    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initializes a new instance of the Animal class.

        Args:
            name (str): The name of the animal.
            hunger (int, optional): The initial hunger level of the animal. Defaults to 0.
        """
        self._name = name
        self._hunger = hunger
    
    def get_name(self):
        """
        Returns the name of the animal.

        Returns:
            str: The name of the animal.
        """
        return self._name
    
    def is_hungry(self):
        """
        Checks if the animal is hungry.

        Returns:
            bool: True if the hunger level is greater than 0, False otherwise.
        """
        return self._hunger > 0
    
    def feed(self):
        """
        Feeds the animal by decrementing the hunger level by 1.

        The hunger level cannot go below 0.
        """
        self._hunger = max(0, self._hunger - 1)

    def talk(self):
        """
        Makes the animal talk.

        This method is meant to be overridden by subclasses.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the animal.

        Returns:
            str: The type name and the name of the animal.
        """
        return type(self).__name__ + " " + self._name
    