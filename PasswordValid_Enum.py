'''
CHECK PASSWORD VALIDITY:
Write a Python program to check the validity of password input by users.
- At least 1 letter between [a-z] and 1 letter between [A-Z].
- At least 1 number between [0-9].
- At least 1 character from [$#@_^&*].
- Minimum length of 8 characters.
- Maximum length 16 characters.
'''

from enum import IntEnum


SPECIAL_CHARS = "!@#$%^&*()-+_"

'''
Write a Python program to check the validity of password input by users.
- At least 1 letter between [a-z] and 1 letter between [A-Z].
- At least 1 number between [0-9].
- At least 1 character from [$#@_^&*].
- Minimum length of 8 characters.
- Maximum length 16 characters.
'''

class PasswordConditions(IntEnum):
    """
    This class will store the index of password conditions
    """
    NUMBER = 0
    LOWERCASE = 1
    UPPERCASE = 2
    SPECIAL_CHAR = 3


def valid_password(password):
    if len(password) > 16 or len(password) < 8:
        return False

    password_checks = [False] * len(PasswordConditions)

    for char in password:
        if char.isdigit():
            password_checks[PasswordConditions.NUMBER] = True
        elif char.isupper():
            password_checks[PasswordConditions.UPPERCASE] = True
        elif char.islower():
            password_checks[PasswordConditions.LOWERCASE] = True
        elif char in SPECIAL_CHARS:
            password_checks[PasswordConditions.SPECIAL_CHAR] = True
        else:
            return False

    return all(password_checks)

#Driver Code
user_password = input("Enter Password:\n")
if valid_password(user_password):
    print("Valid Password")
else:
    print("Invalid Password")