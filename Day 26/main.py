# Exercise 1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [num * num for num in numbers]
#
#
# #Write your code 👆 above:
#
# print(squared_numbers)

# Exercise 2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
# result = [num for num in numbers if num % 2 == 0]
#
#
# #Write your code 👆 above:
#
# print(result)


# # Exercise 3
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
# print(list1)
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
# print(list2)
#
# result = [int(num) for num in list1 if num in list2]
#
# # Write your code above 👆
#
# print(result)


# # Exercise 4 Dictionary Comprehension
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# sentence_list = sentence.split()
# result = {word: len(word) for word in sentence_list}
#
#
# print(result)

# # Exercise 5 Dictionary Comprehension

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}


print(weather_f)
