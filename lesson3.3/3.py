from random import randint

data = [randint(-10, 10) for x in range(5)]


def foo(x):
    return x > 0

filtered = list(filter(lambda x: x > 0, data))

print(data)
print(filtered)
