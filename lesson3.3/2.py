# Lambda


# def foo():
#     ...


# lambda parameters : expression


two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x * y


def two():
    return 2


def sqr(x):
    return x * x


def pwr(x, y):
    return x * y


# (two())
# print(sqr(10))
# print(pwr(10, 20))


numbers = [1, 2, 3, 4, 5]
sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)


players = [
    {"name": "Mike", "age": 32},
    {"name": "John", "age": 87},
    {"name": "Stue", "age": 31},
    {"name": "Frank", "age": 12},
]

# BAD idea !!!!
# new_players = []
# for player in players:
#     new_players.append(player.get("age"))

from pprint import pprint


def foo(x):
    return x.get("name")


# foo = lambda x: x.get("name")
# foo("John")

sorted_players = sorted(players, key=lambda x: x.get("age"))
# sorted_players = sorted(players, key=foo)
# pprint(sorted_players)


# def sorted(iterable, key=function_object):
#     for i, next_i in iterable:
#         key(i) > key(next_i)

list_1 = [x for x in range(10) if x % 2 == 0]


list_2 = list(map(lambda x: x*2, range(10)))

print(list_1)
print(list_2)
