# print("Welcome to the roller coaster!")
# height = int(input("what is your height in cm? "))
#
# if height>120:
#     print("You can ride on the rollercoaster!")
# else:
#     print("Go home!!!")

# # <editor-fold desc="Description">
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# result = number % 2
#
# if result > 0:
#     print("This is an odd number!")
# else:
#     print("This is an even number!")
# # </editor-fold>

# print("Welcome to the roller coaster!")
# height = int(input("what is your height in cm? "))
#
# if height >= 120:
#     print("You can ride on the rollercoaster!")
#     age = int(input(("What is your age? ")))
#     if age < 12:
#         print("please pay $5.")
#     elif 12 < age < 18:
#         print("please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride!!!")

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# bmi = int(weight / (height**2))
#
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight!")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normal weight!")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are overweight!")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese!")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese!")

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year!")
#         else:
#             print("Not Leap year!")
#     else:
#         print("Leap Year!")
# else:
#     print("Not Leap year!")

#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is {bill}")
#
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
# else:
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is {bill}")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# #
# # lowerName1 = name1.lower()
# # lowerName2 = name2.lower()
# #
# # count1 = 0
# # count1 =+ lowerName1.count("t")
# # count1 =+ lowerName1.count("r")
# # count1 =+ lowerName1.count("u")
# # count1 =+ lowerName1.count("e")
# # count1 =+ lowerName1.count("l")
# # count1 =+ lowerName1.count("o")
# # count1 =+ lowerName1.count("v")
# # count1 =+ lowerName1.count("e")
# #
# # count2 = 0
# # count2 += lowerName2.count("t")
# # count2 += lowerName2.count("r")
# # count2 += lowerName2.count("u")
# # count2 += lowerName2.count("e")
# # count2 += lowerName2.count("l")
# # count2 += lowerName2.count("o")
# # count2 += lowerName2.count("v")
# # count2 += lowerName2.count("e")
# #
# # total = str(count1) + str(count2)
# # value = int(total)
# #
# # if value > 90 or value < 10:
# #     print(f"Your score is {value}, you go together coke and mentos.")
# # elif 40 < value < 50:
# #     print(f"Your score is {value}, you are alright together.")
# # else:
# #     print(f"Your score is {value}.")
# combine = name1.lower() + name2.lower()
# count1 = 0
# count2 = 0
# count1 += combine.count("t")
# count1 += combine.count("r")
# count1 += combine.count("u")
# count1 += combine.count("e")
#
# count2 += combine.count("l")
# count2 += combine.count("o")
# count2 += combine.count("v")
# count2 += combine.count("e")
#
# total = str(count1) + str(count2)
# value = int(total)
#
# if value > 90 or value < 10:
#     print(f"Your score is {value}, you go together coke and mentos.")
# elif 40 <= value <= 50:
#     print(f"Your score is {value}, you are alright together.")
# else:
#     print(f"Your score is {value}.")

##FINAL CHALLLENGE

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if choice1.lower() == "left":
    choice2 = input('you\'re come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                    'boat. Type "swin" to swin across.\n')
    if choice2.lower() == "wait":
        choice3 = input("You arrive at the island unharmed. there is a house with 3 doors. One red, one yellow and "
                        "one blue. Which colour do you choose?\n")
        if choice3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3.lower() == "yellow":
            print("You found the treasure! You win!")
        elif choice3.lower() == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You choose a door that doesn't exist. Game over!")
    else:
        print("You got attacked by a angry trout. Game over!")

else:
    print("You fell into a hole. Game over")
