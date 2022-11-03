def add(*args):
    total = 0
    for num in args:
        total += num

    return total


print(add(4, 8, 1, 3, 9, 5))


def calculated(**kwargs):
    total = kwargs["add"] + 1
    total = total * kwargs["multiply"]
    return total


print(calculated(add=3, multiply=6))

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]


class Car:
     def __init__(self, **kwargs):
         self.make = kwargs.get("make")
         self.model = kwargs.get("model")

#my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
print(my_car.model)