import pandas as pd

sq_data = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
save_filtered_data = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//squirrel_count.csv"


# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela" ],
#     "scores": [76,56,65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv(new_file_to_save_csv_file)

# read the data from squirrel data
data_from_sq = pd.read_csv(sq_data)
fur_color_data = data_from_sq["Primary Fur Color"]
print(gray)






# data_dict = {
#     "Fur color": []
# }
