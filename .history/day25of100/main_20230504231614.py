import csv
csv_file = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//weather_data.csv"

with open(csv_file, newline="") as csvfile:
    reader = csv.reader(csvfile)

    data_list = []    

    for row in reader:
        data_list.append(row)




with open(csv_file, "r") as file:
    reader = csv.reader(file)
    temperature =  [row[1] for row in reader]




print(temperature)