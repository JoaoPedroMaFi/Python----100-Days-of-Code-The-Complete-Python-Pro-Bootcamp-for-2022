# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#     print(fruits)

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
#
# #Write your code below this row 👇
#
# #student_heights = 180 124 165 173 189 169 146
#                     #156 178 165 171 187
# average1 = sum(student_heights)/float(len(student_heights))
# total_height = 0
# total_students = 0
# for height in student_heights:
#     total_students += 1
#     total_height += height
#
# average2 = total_height/float(total_students)
#
# print(average1)
# print(average2)

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# # 78 65 89 86 55 91 64 89
# bigger = 0
# for score in student_scores:
#     if score > bigger:
#         bigger = score
#
# print(bigger)
# print(max(student_scores))
#
# print(f"The highest score of class is : {bigger}")

# for number in range(1, 11, 2):
#     print(number)
#
# total = 0
# for number in range (1, 101):
#     total += number
#
# print(total)

# #Write your code below this row 👇
# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)


# #Write your code below this row 👇
#
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = []
# for n in range(0, nr_letters):
#     password.append(letters[random.randint(0, len(letters) - 1)])
# print(password)
# for n in range(0, nr_symbols):
#     password.append(symbols[random.randint(0, len(symbols) - 1 )])
# print(password)
# for n in range(0, nr_numbers):
#     password.append(numbers[random.randint(0, len(numbers) - 1)])
# print(password)
#
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#
# password = []
# for n in range(0, nr_letters):
#     password.append(letters[random.randint(0, len(letters) - 1)])
# for n in range(0, nr_symbols):
#     password.append(symbols[random.randint(0, len(symbols) - 1 )])
# for n in range(0, nr_numbers):
#     password.append(numbers[random.randint(0, len(numbers) - 1)])
# print(password)
#
# for n in range(0, len(password)):
#     position1 = random.randint(0, len(password) - 1)
#     position2 = random.randint(0, len(password) - 1)
#     a = password[position1]
#     b = password[position2]
#     c = a
#     a = b
#     b = c
#     password[position1] = a
#     password[position2] = b
#
# print(password)
