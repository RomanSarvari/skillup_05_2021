
def wrapper(*args, **kwargs):
    print(args, kwargs)
    def pretty(func):
        def inner():
            print('-------------')
            func()
            print('-------------')
        return inner
    return pretty



@wrapper(1,2,34,5, foo='bar')
def foo():
    print("Hello world")



foo()
