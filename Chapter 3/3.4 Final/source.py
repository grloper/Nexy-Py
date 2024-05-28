import string

# Default exception for length errors
from Exceptions.UsernameTooShort import UsernameTooShort
from Exceptions.PasswordTooShort import PasswordTooShort
from Exceptions.PasswordTooLong import PasswordTooLong
from Exceptions.UsernameTooLong import UsernameTooLong

# Exceptions for missing characters in the password
from Exceptions.PasswordMissingCharacter.MissingDigit import MissingDigit
from Exceptions.PasswordMissingCharacter.MissingLowercase import MissingLowercase
from Exceptions.PasswordMissingCharacter.MissingSpecialCharacter import MissingSpecialCharacter
from Exceptions.PasswordMissingCharacter.MissingUppercase import MissingUppercase

# Exception for illegal characters in the username, and the index of the first illegal character
from Exceptions.UsernameContainsIllegalCharacter import UsernameContainsIllegalCharacter


def is_valid_username(username):
    """
    Checks if a username is valid.

    Args:
        username (str): The username to be checked.

    Raises:
        UsernameContainsIllegalCharacter: If the username contains an illegal character.
        UsernameTooShort: If the username is too short (less than 3 characters).
        UsernameTooLong: If the username is too long (more than 16 characters).

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    # Check if all characters are valid = ascii letters, digits, or underscore
    if not (all(c in string.ascii_letters + string.digits + "_" for c in username)): 
        # Find the first illegal character
        illegal_char_index = next((i for i, c in enumerate(username) if c not in string.ascii_letters + string.digits + "_"), -1) 
        if illegal_char_index != -1: # If an illegal character was found
            raise UsernameContainsIllegalCharacter(username[illegal_char_index], illegal_char_index)
    elif len(username) < 3: # Check if the username is too short
        raise UsernameTooShort()
    elif len(username) > 16: # Check if the username is too long
        raise UsernameTooLong()
    return True


def is_valid_password(password):
    """
    Checks if a password is valid based on the following criteria:
    - Length should be between 8 and 40 characters.
    - Should contain at least one lowercase letter.
    - Should contain at least one uppercase letter.
    - Should contain at least one digit.
    - Should contain at least one special character.

    Args:
        password (str): The password to be validated.

    Raises:
        PasswordTooShort: If the password length is less than 8 characters.
        PasswordTooLong: If the password length is greater than 40 characters.
        MissingLowercase: If the password does not contain any lowercase letters.
        MissingUppercase: If the password does not contain any uppercase letters.
        MissingDigit: If the password does not contain any digits.
        MissingSpecialCharacter: If the password does not contain any special characters.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if not (8 <= len(password) <= 40): # Check if the password length is within the valid range
        raise PasswordTooShort() if len(password) < 8 else PasswordTooLong()
    # Check if the password contains at least one lowercase, uppercase, 
    # digit, and special character
    elif not any(char.islower() for char in password):
        raise MissingLowercase()
    elif not any(char.isupper() for char in password):
        raise MissingUppercase()
    elif not any(char.isdigit() for char in password):
        raise MissingDigit()
    elif not any(char in string.punctuation for char in password):
        raise MissingSpecialCharacter()
    return True
    


def check_input(username, password):
    """
    Validates the given username and password.

    Parameters:
    - username (str): The username to be validated.
    - password (str): The password to be validated.

    Raises:
    - PasswordTooShort: If the password is too short.
    - PasswordTooLong: If the password is too long.
    - MissingUppercase: If the password is missing an uppercase letter.
    - MissingLowercase: If the password is missing a lowercase letter.
    - MissingDigit: If the password is missing a digit.
    - MissingSpecialCharacter: If the password is missing a special character.
    - UsernameContainsIllegalCharacter: If the username contains an illegal character.
    - UsernameTooShort: If the username is too short.
    - UsernameTooLong: If the username is too long.

    Prints "OK" if the username and password are valid.
    Prints an error message if any validation errors occur.
    """
    try:
        is_valid_username(username) # Check if the username is valid
        is_valid_password(password) # Check if the password is valid
        print("OK")
        # Handle the different exceptions that can be raised by the password validation 
    except (PasswordTooShort, PasswordTooLong, MissingUppercase, MissingLowercase, MissingDigit, MissingSpecialCharacter) as e:
        print(f"Error: {str(e)}")
        # Handle the username exceptions
    except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong) as e:
        print(f"Error: {str(e)}")



def main():
    # Test cases
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == "__main__":
    main()
