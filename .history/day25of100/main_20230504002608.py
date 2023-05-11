import csv
csv_file = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//weather_data.csv"

with open(csv_file, newline="") as csvfile:
    reader = csv.reader(csvfile)

    data_list = []

    for row in reader:
        data_list.append(row)
    

for _ in data_list:
    print(data_list[0])