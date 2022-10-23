import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super.__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # random colors to food
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color((r, g, b))
        # random location for food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.dot(random_x, random_y)

