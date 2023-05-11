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
all_color_list = data_from_sq["Primary Fur Color"].to_list()


# Count occurrences of elements in the list
element_counts = {}
for element in all_color_list:
    element_counts[element] = all_color_list.count(element)

print(type(element_counts))
# Print the element counts
for element, count in element_counts.items():
    print(f"{element}: {count}")


# print(all_color_list)

# data_dict = {
#     "Fur color" : ["gray", ""]
#     }

# data = pd.DataFrame(element_counts)
# data.to_csv(save_filtered_data)
# data=pd.DataFrame([element_counts], index=[0])
# data.to_csv(save_filtered_data, index=False)
my_list = [element_counts]

grat = [d["Gray"] for d in my_list]

print(nan_values)







# data_dict = {
#     "Fur color": []
# }
