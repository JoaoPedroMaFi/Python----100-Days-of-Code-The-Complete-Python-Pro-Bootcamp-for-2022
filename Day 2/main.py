# #Data Types
#
# #string
#
# print("Hello"[4])
#
#
# #Intenger
#
# print(11223 + 6536434)
#
# print(123_111_222)
#
# #Float
#
# 3.1415
#
#
# #Bollean
#
# print(True)
# print(False)
#
#
#
# num_char = len(input("What is your name?"))
#
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")
#
# print(type(num_char))

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆
#
# ####################################
# # Write your code below this line 👇
#
# if type(two_digit_number == str) and len(two_digit_number) == 2:
#     a = int(two_digit_number[0])
#     b = int(two_digit_number[1])
#     print(a + b)

#
# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 * 3 / 3 * 3))
# print(3 * (3 + 3 / 3 - 3))

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# a = float(weight)
# b = float(height)
# bmi = (a/(b**2))
# bmi_as_int = int(bmi)
#
# print(bmi_as_int)

# print(round(8 / 3, 5))
# print(8 // 3)
#
# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
#
# years_left = 90 - int(age)
#
# total_months = years_left * 12
# total_weeks = years_left * 52
# total_days = years_left * 365
#
# print(f"You have {total_days} days, {total_weeks} weeks, and {total_months} months left.")

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator. ")
bill = input("What was the total bill? ")
percentage = input("What the percentage tip would youi like to give? 10, 12, or 15 ")
people = input("How many people to split the bill? ")

total_percentage = 1.0 + (float(percentage) / 100)
total = float(bill) * total_percentage
per_people = round(float(total) / float(people), 2)

print(f"Each person should pay: {per_people}")
