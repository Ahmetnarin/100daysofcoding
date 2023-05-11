import csv
csv_file = "C:\Users\AHNARIN\Desktop\Ahnarin\100_days_of_coding\day25of100\weather_data.csv"

with open("weather_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)

    data_list = []

    for row in reader:
        data_list.append(row)
    

print(data_list)