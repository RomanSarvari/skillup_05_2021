def task_1():
    text = """“Don't compare yourself with anyone in this world... if you do so, you are insulting yourself.”
                                                                             Bill Gates"""
    print(text)


# task_1()


def task_2(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)


# task_2(a=10, b=20)


def task_3(side, sign, fill, space=" ", min_side_len=3):
    if side < min_side_len:
        print("Side have to be greater than 3")
        return None
    if fill:
        for i in range(side):
            print(sign * side)
    else:
        print(sign * side)
        for i in range(side - 2):
            print(sign + space * (side - 2) + sign)
        print(sign * side)


# task_3(side=20, sign="*", fill=False)

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********


def task_4(a, b, c, *args):
    print(args)

# task_4(2, 3, 4, 5, 6, 6)

def create_record(a=None, *args, **kwargs):
    print(kwargs)


# create_record(title="Artist", row="ACDC")


players = []

def save_player(**kwargs):
    players.append(kwargs)


save_player(name="Jordan", age=12)
save_player(name="Mike", heigh=2.00)


# print(players)


def task_5(number):
    text = str(number)
    if len(text) % 2 != 0:
        return False
    first_part = text[:len(text)//2]
    second_part = text[len(text)//2:]

    result = first_part == second_part[::-1]

    return result



result = task_5(123321)

print(result)
