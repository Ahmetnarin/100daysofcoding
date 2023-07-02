# with open("a_file.txt") as data_file:
#     data_file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt" , "a")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

fruits = [ "Apple" , "Pear" , "Orange" ]

def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


try:
    make_pie(6)
except IndexError:
    # show last element if index number bigger than array size
    make_pie(-1)
    print("You type an index which is not exist.")
except TypeError:
    print("Your input is not a index number which indicates a fruit")
except KeyError:
    print("You type an index which is not exist.")

else:
    print("Your input is not a index number which indicate a fruit")


