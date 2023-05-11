my_list = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Mike', 'age': 35}]

# Separate the values of 'name' key from the list of dictionaries
name_values = [d['name'] for d in my_list]

# Separate the values of 'age' key from the list of dictionaries
age_values = [d['age'] for d in my_list]

print(name_values)
print(age_values)
