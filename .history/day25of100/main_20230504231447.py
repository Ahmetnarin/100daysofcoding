import csv
csv_file = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//weather_data.csv"

with open(csv_file, newline="") as csvfile:
    reader = csv.reader(csvfile)

    data_list = []
    temperature = []
    

    for row in reader:
        data_list.append(row)




with open(csv_file, "r") as file:
    reader = csv.reader(file)


print(temperature)