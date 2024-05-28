class PasswordMissingCharacter(Exception):
    def __init__(self):
        self.message = "The password is missing a character"

    def __str__(self):
        return self.message