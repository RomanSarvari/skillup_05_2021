from pprint import pprint

a = 20
def pprint(text):
    print("**********")
    print(text)

def pprint(text):
    print("-----------")
    print(text)

def foo():
    a = 10
    pprint(a)
    
def bar():
    pprint(a)
    
    
foo()
bar()
