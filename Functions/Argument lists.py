# Argument lists in Python.

def main():
    x = ('meow', 'grr', 'purr', 'sleep', 'nap', 'walk')
    kitten(*x)


# Note: *args here is useful when you when you want to pass many
# arguments to your function and you do not know how many of them.

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')


if __name__ == '__main__': main()
