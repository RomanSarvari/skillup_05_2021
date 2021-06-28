# def mul(a, b):
#     return a * b

# mul(3, 4)


def mul(a):
    def inner(b):
        return a * b
    return inner


mul2 = mul(2)
mul3 = mul(3)

var1 = mul2(5)
var2 = mul3(5)

# print(var1)
# print(var2)

def fun1(a):
    x = a * 3
    def fun2(b):
        nonlocal x
        return b + x
    return fun2

# test_fun = fun1(4)

# print(test_fun(7))


x = 10

def foo():
    global x
    x = 20
    print(x)

foo()
print(x)
