# print("I am from the new group")


def foo(a, b, c, s):
    allowed_operations = {
        "product": "*",
        "sum": "+"
    }
    if s not in allowed_operations.values():
        return "Operation not allowed"
    if s == allowed_operations["sum"]:
        return a + b + c
    elif s == allowed_operations["product"]:
        return a * b * c


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
s = input("Enter + or *: ")

n = foo(a, b, c, s)

print(n)