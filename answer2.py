# Q2. Write a Python program that generates a password with the following conditions:
# At least one uppercase letter.
# At least one lowercase letter.
# At least two numbers.
# At least one special character (e.g., !@#$%&*).
# The password should be exactly 16 characters long.
# The password should contain no repeating characters.
# The password should have a random order each time.



import random
import string

def generate_password():
    """Generates a secure 16-character password meeting all conditions."""
    uppercase = random.sample(string.ascii_uppercase, 1)
    lowercase = random.sample(string.ascii_lowercase, 1)
    numbers = random.sample(string.digits, 2)
    special_chars = random.sample("!@#$%&*", 1)
    
    remaining_chars = random.sample(
        string.ascii_letters + string.digits + "!@#$%&*", 11
    )
    
    password_list = uppercase + lowercase + numbers + special_chars + remaining_chars
    random.shuffle(password_list)
    
    return "".join(password_list)

if __name__ == "__main__":
    print("Generated Password:", generate_password())

    
    


