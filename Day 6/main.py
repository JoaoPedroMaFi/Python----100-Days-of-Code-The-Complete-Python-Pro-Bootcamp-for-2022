# print("Hello")
# print(len("hello"))


# def my_function():
#     print("Hello")
#     print("Bye")
#
#
# my_function()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if not wall_on_right() and not wall_in_front():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()
