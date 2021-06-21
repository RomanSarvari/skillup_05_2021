from pprint import pprint


source_dict = {
    "key": "value",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
}

def pprint(anything):
    print("*********")
    print(anything)
    print("*********")

pprint(source_dict)

# print(locals())
# print(globals())
print(vars())

del pprint

# print(locals())

# pprint(source_dict)
