# A function that is associated with a class is called a method.
# This provides the interface to the class and its objects.


class Animal:

    # init is a special class method name, with double underscores before and after.
    # And that's a special name for a class function which operates as an initializer, or a constructor.
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    #  Notice that the object variables are named with a leading underscore, and this again is traditional.
    #  Python doesn't have private variables, and so there's no way to actually prevent somebody from using these.
    #  this indicates that it's a private variable and it should not be set or retrieved outside of the setter getter.
    def type(self, t=None):
        if t: self._type = t
        return self._type

    def name(self, n=None):
        if n: self._name = n
        return self._name

    def sound(self, s=None):
        if s: self._sound = s
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


# This is a specially-named method, which provides the string representation of the object.
# And this allows us to print it with simply this print and the object like that, without needing a special function.
def __str__(self):
    return f'The {self.type()} is named "{self.name()} and says "{self.sound()}'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rawr')
    a1 = Animal(type='duck', name='donald', sound='quack')
    a0.sound('bark')
    print_animal(a0)
    print_animal(a1)


if __name__ == '__main__': main()
