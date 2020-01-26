# Function arguments in Python.
# Note: default argument must follow non-default argument
# Note: In Python, when changing a value of mutable it
# get aso changed in another reference of that immutable. (Call by Reference)

# def main():
#     x = [5]
#     y = x
#     y[0] = 3
#     print(id(x))
#     print(id(y))
#     print(x)
#     print(y)
#     # kitten(x)
#     # print(f'in main: x is {x}')
#
# def kitten(a):
#     print(id(a))
#     a = 3
#     print(id(a))
#     print('Meow.')
#     print(a)

def main():
    x = [5]
    kitten(x)
    print(f'in main: x is {x}')


def kitten(a):
    a[0] = 3
    print('Meow.')
    print(a)


if __name__ == '__main__': main()
