# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# colours = data["Primary Fur Color"].tolist()
# new_list = {}
# for color in colours:
#     if color not in new_list:
#         new_list[color] = 1
#     else:
#         new_list[color] += 1
#
# print(new_list)
# final_dict = {}
# final_dict["color"] = []
# final_dict["count"] = []
# for item in new_list:
#     final_dict["color"].append(item)
#     final_dict["count"].append(new_list[item])
#
# print(final_dict)
#
# df = pandas.DataFrame(final_dict)
# df.to_csv("new_file.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")