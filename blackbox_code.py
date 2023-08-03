import random
import string


def generate_password(length):
    # Define the characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the given length
    password = ''.join(random.choice(chars) for i in range(length))

    return password


# Test the function with a password length of 12
password = generate_password(12)
print(password)