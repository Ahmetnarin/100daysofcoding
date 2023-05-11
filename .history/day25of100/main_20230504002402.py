import csv

with open("weather_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)

    data_list = []