class PasswordTooShort(Exception):
    def __init__(self):
        self.message = "Password must be at least 8 characters long"

    def __str__(self):
        return self.message