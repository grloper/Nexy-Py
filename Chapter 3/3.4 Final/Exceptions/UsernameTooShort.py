class UsernameTooShort(Exception):
    def __init__(self):
        self.message = "Username must be at least 3 characters long"

    def __str__(self):
        return self.message