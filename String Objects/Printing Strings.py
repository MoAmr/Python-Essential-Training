# Strings are first class objects in Python 3.


class MyString(str):
    def __str__(self):
        return self[::-1]


print('Hello World.'.upper())
print('Hello World.'.swapcase())
print('Hello World. {}'.format(42 * 7))
# print("""
#         Hello,
#         World.
#
#         {}
#         """.format(42 * 7))
s = 'Hello World. {}'
print(s.format(42 * 7))

s1 = MyString('Hello, World.')
print(s1)
