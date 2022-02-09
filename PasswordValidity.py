"""
Write a Python program to check the validity of password input by users.
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@_^&*].
Minimum length of 8 characters.
Maximum length 16 characters.
"""
#TIME COMPLEXITY: O(N)

def is_password_valid(n, password):
    if n < 8 and n >16:
        return False

    special_characters = "!@#$%^&*()-+_"
    digit = lower =  upper = special_char = False 

    
    for char in password:
        if char.isdigit():
            digit = True
        elif char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char in special_characters:
            special_char = True
        else:
            return False

    return digit and lower and upper and special_char
 
#Driver Code
if __name__ == '__main__':
    password = input("Enter Password:\n")
    n = len(password)  # stores the length of the input password
    is_valid = is_password_valid(n, password) 
    if is_valid:
        print(f"{password} is a valid password.")
    else:
        print(f"{password} is an invalid password. Try Again.")