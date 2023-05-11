import pandas as pd

sq_data = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"


# read the data from squirrel data
data_from_sq = pd.read_csv(sq_data)
fur_color_data = data_from_sq["Primary Fur Color"]
