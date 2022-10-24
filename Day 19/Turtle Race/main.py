import random
from tkinter import messagebox
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

str_colors = ""
for color in colors:
    str_colors += color + "\n"

messagebox.showinfo(title="All colors available!", message=str_colors)
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Enter a color:  ").lower()

all_turtles = []
high = -70
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-238, y=high)
    high += 30
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            if user_bet == turtle.pencolor():
                messagebox.showinfo("You Win! The Winner is:", f"{turtle.pencolor()}")
            else:
                messagebox.showinfo("You lose!", f"The winner is {turtle.pencolor()}")
            is_race_on = False

screen.exitonclick()
