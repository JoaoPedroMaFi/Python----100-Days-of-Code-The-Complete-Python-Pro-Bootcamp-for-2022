# with open("weather_data.csv") as data_file:
#     data= data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# # print(data_dict)
# # print((data))
# data_list = data["temp"].tolist()
# print(data_list)
# average = sum(data_list)/ len(data_list)
# print(average)
# average1 = data["temp"].mean()
# print(average1)
#
# max_value = data["temp"].max()
# print(max_value)
# data.day
#
#
# #Get Data in columns
# print(data.condition)


#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
monday_temp = monday["temp"]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)