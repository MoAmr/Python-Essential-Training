# Keyword Arguments in Python.
# Keyword Arguments ae like List Arguments that are Dictionaries instead of Tuples.

def main():
    x = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    kitten(**x)


# Note: the two ** means that the argument being passed is keyword reference.

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow.')


if __name__ == '__main__': main()
