def pow(mul):
    def sqare(func):
        def inner(a, b):
            var = func(a, b)
            return var ** mul
        return inner
    return sqare

@pow(2)
def sum(a, b):
    return a + b

@pow(3)
def dif(a, b):
    return a - b

# Этих строк очень много
c = sum(10, 20)
z = dif(15, 23)

print(c)
print(z)
