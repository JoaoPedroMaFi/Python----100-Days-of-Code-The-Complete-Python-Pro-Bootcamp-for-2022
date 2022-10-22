import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")


# timmy_the_turtle.forward(122)
# timmy_the_turtle.right(90)

# for _ in range(0,4):
#     tim.forward(122)
#     tim.right(90)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for i in range(3, 15):
#     tim.color(random.choice(colours))
#     for j in range(i):
#         tim.forward(100)
#         angle = 360 / i
#         tim.right(angle)


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.speed(0)
# tim.pensize(15)
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# directions = [0, 90, 180, 270]
# tim.speed(0)
# tim.pensize(15)
# turtle.colormode(255)
# for _ in range(1000):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     print(color)
#     tim.pencolor(color)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turtle.colormode(255)
tim.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        current_heading = tim.heading()
        tim.circle(100)
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(1)

screen = Screen()
screen.exitonclick()
