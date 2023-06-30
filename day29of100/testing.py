def save_file(*args):
    for arg in args:
        with open("passwords.txt", "w") as file:
            file.write(arg + "\n")


save_file("hello" , "world", "bitch")