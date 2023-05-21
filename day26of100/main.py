file1 = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day26of100//file1.txt" 
file2 = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day26of100//file2.txt"

file1_values = []
file2_values = []


with open(file1, 'r') as file:
    for line in file:
        number = int(line)
        file1_values.append(number)

with open(file2, 'r') as file:
    for line in file:
        number = int(line)
        file2_values.append(number)

print(file1_values)
print(file2_values)

result = [x for x in file1_values if x in file2_values]


print(result)