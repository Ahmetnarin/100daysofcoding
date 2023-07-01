# with open("a_file.txt") as data_file:
#     data_file.read()

try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt" , "a")
    file.write("Something")
    # print("There was an error")
