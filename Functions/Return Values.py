# Return Values in Python.
# Note: in Python there is no distinction between a function or a procedure

def main():
    x = kitten()
    print(type(x), x)


def kitten():
    print('Meow.')
    return dict(x=24, y=43, z=44)


if __name__ == '__main__': main()
