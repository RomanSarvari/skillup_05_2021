# element 3
# i 2


def simple(l: list) -> int:
    counter = 0
    for element in l:
        l2 = any([True if element % i != 0 else False for i in range(2, element)])
        if l2:
            counter += 1
    return counter


r = simple([1, 2, 3, 4, 5, 6, 7])
print(r)
