
def password_is_valid(password: str)-> bool:
    if len(password) < 8:
        return False
    return True


password_1 = '123123'
password_2 = 'qweopoqwie123'

l = list()

# print(password_is_valid(password=password_1))
# print(password_is_valid(password=password_2))

def foo(name="admin") -> None:
    """BLABLA"""
    print(name)

foo("Dima")
foo()
