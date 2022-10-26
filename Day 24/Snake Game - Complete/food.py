import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        # random colors to food
        r = random.randint(15, 240)
        g = random.randint(15, 240)
        b = random.randint(15, 240)
        self.screen.colormode(255)
        self.color((r, g, b))
        # random location for food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
