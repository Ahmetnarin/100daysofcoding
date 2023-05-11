# import csv
csv_file = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//weather_data.csv"

# with open(csv_file, newline="") as csvfile:
#     reader = csv.reader(csvfile)

#     data_list = []    

#     for row in reader:
#         data_list.append(row)



# # open the file in read mode
# with open(csv_file, "r") as file:
#     # Create a csv reader object
#     reader = csv.reader(file)
#     # Extract the desired column (in this case "1") using list comprehension
#     temperature =  [row[1] for row in reader]




# print(temperature)

import pandas 

data = pandas.read_csv(csv_file)
print(data["temp"])
print(data["day"])

data_dict = data.to_dict()
print(data_dict)

print(len(data["temp"].to_list()))
print(len(data["day"].to_list()))

average_temp = data["temp"].mean()
max_value = data["temp"].max()

print()
print()
print(type(average_temp) )
print(max_value)
print(len(data.day ))

# get the data from a row
print(data[data.temp == max_value])

def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

# get the monday temperature and convert into fahrenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)

print(f"{monday_temp} converted into fahrenheit {celcius_to_fahrenheit(monday_temp)}")

# Create a dataframe from scratch
data_dict = {
    "students": [[]]
}


