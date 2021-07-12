def foo():
    var = 100

    def bar():
        nonlocal var
        var += 100

    bar()
    print(var)


foo()
