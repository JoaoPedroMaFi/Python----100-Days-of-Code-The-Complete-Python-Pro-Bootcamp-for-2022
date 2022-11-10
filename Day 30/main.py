# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# keyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existente_key"]

# IndexError
# fruits_list = ["Apple", "Banana", "Pear"]
# fruit = fruits_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that ia came up")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)


# Exercise
#
# fruits = ["Apple", "Pear", "Orange"]
#
#
# # !ODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(2)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         likes = post["Likes"]
#         total_likes = total_likes + likes
#     except KeyError:
#         pass
#     # else:
#     #     total_likes = total_likes + likes
#
#
# print(total_likes)
