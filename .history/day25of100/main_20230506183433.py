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

data_dict = data.to_dict()
print(data_dict)

print(data["temp"].to_list())
print(data["day"].to_list())

