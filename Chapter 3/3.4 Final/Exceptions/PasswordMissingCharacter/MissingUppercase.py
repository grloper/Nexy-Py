from .PasswordMissingCharacter import PasswordMissingCharacter

class MissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"