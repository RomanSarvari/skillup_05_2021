# cache = {1: 1, 2: 1}
# def fib(n):
#     result = cache.get(n)
#     if not result:
#         result = fib(n-2) + fib(n-1)
#         cache[n] = result
#     return result


from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

# print(fib(113))


# f(x, y, z) => f(x)f(y)f(z)

from functools import wraps

def decor(func):
    @wraps(func)
    def wrapper(name):
        print("*****")
        func(name)
        print("======")
    return wrapper



@decor
def greeting(name):
    print(f"Hi, {name}")

@decor
def greeting_2(name):
    print(f"Hello, {name}")


greeting(name="Dima")
greeting_2(name="Dima")
