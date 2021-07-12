def outer_func():
    var = 100

    def inner_func():
        print(f"Printing var from inner_func(): {var}")

    inner_func()
    another_var = 200

    print(dir())
    print(f"Printing var from outer_func(): {var}")


print(dir())

outer_func()

