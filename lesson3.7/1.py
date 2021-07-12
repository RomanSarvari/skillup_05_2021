# Pizza -> tomato, cheese, size

# def foo():
#     return 1
#
# class Car:
#     def __init__(self):
#         pass
#
#     def get_name():
#         pass
#
#     # pass
#     # # price = 100
#     # color = ''
#     # # weight = 1500
#     # # engine = 1.5
#
# bmw = Car()
# mers = Car()
#
# bmw.get_name()
# Car.get_name(bmw)
# Car.get_name(mers)


class Dog:
    def __init__(self, name="Unnamed dog", age=0, alive=True):
        self.sound = "Wof"
        self.age = age
        self.name = name
        self.alive = alive

    def description(self):
        return f"Hello my name is {self.name}, I am {self.age}"

    def speak(self):
        if self.alive:
            return f"{self.sound} {self.sound}"
        else:
            return f"{self.name} is dead"


mikey = Dog(name="Mikey", age=10)
mikey.type = 'New dog type'

ron = Dog(name="Ron", age=4, alive=False)
billy = Dog()

print(mikey.description())
print(mikey.speak())
print(mikey.type)

print(ron.description())
print(ron.speak())
print(ron.type)

print(billy.description())
print(billy.speak())