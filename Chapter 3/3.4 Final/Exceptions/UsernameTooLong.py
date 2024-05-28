class UsernameTooLong(Exception):
    def __init__(self):
        self.message = "Username must be at most 16 characters long"

    def __str__(self):
        return self.message