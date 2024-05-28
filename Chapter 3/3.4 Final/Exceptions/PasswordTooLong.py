class PasswordTooLong(Exception):
    def __init__(self):
        self.message = "Password must be at most 40 characters long"

    def __str__(self):
        return self.message