import csv
csv_f

with open("weather_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)

    data_list = []

    for row in reader:
        data_list.append(row)
    

print(data_list)