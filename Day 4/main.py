import random

# import my_module
#
# random_intenger = random.randint(1,10)
# print(random_intenger)
#
# print(my_module.pi)
#
# random_float = random.random() * 5
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")


# #Write your code below this line 👇
# #Hint: Remember to import the random module first. 🎲
#
# coin = random.randint(0, 1)
#
# if coin == 0:
#     print("Tails")
# else:
#     print("Heads")

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# print(states_of_america)
# states_of_america.append("Angelland")
# print(states_of_america)
# states_of_america.extend(["Bankai", "Jack bauer land"])
# print(states_of_america)
#
#
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# #Angela, Ben, Jenny, Michael, Chloe
#
# print(names)
# print(len(names))
# #print(names[random.randint(0, len(names)) - 1])
# person = names[random.randint(0, len(names)) - 1]
#
# print(f"{person} is going to buy the meal today.")


# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(len(states_of_america))
# print(states_of_america)
#
# num_of_states = len(states_of_america)
#
# print(states_of_america[num_of_states - 1])
#
#
# #dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
#
# print(dirty_dozen[1][1])

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
# column = int(position[0]) - 1
# row = int(position[1]) - 1
# map[row][column] = "X  ️"
#
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

man_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
pc_choice = random.randint(0, 2)

if man_choice >= 3 or man_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("Your choice")
    if man_choice == 0:
        print(rock)
    elif man_choice == 1:
        print(paper)
    elif man_choice == 2:
        print(scissors)
    else:
        print("Wrong move")

    print("Computer Choice")
    if pc_choice == 0:
        print(rock)
    elif pc_choice == 1:
        print(paper)
    elif pc_choice == 2:
        print(scissors)
    else:
        print("Wrong move")

    if man_choice == 0 and pc_choice == 2:
        print("You win!")
    elif man_choice == 2 and pc_choice == 1:
        print("You win!")
    elif man_choice == 1 and pc_choice == 0:
        print("You win!")
    elif man_choice == 2 and pc_choice == 0:
        print("You loose")
    elif man_choice == 1 and pc_choice == 2:
        print("You loose")
    elif man_choice == 0 and pc_choice == 1:
        print("You loose")
    else:
        print("It's a Draw")
