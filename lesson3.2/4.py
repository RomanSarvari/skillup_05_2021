var = 100

def foo():
    global var
    print(var)

    var = 200


foo()

print(var)
