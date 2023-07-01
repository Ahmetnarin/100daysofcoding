import numpy as np 

def create_array(*args):
    arr = np.array(args)
    with open("passwords.txt" , "w") as file:
        for i in arr:
            file.write(i + " | ")
        file.write("\n-----------------------------------")

create_array("hello" , "world", "bitch", "fdgfedgfde")


import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
generated_password = generate_password()
print("Generated Password:", generated_password)
