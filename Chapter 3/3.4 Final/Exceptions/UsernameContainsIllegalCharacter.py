class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character, index):
        super().__init__(f"Username contains illegal character '{illegal_character}' at index {index}")
        self.illegal_character = illegal_character
        self.index = index
