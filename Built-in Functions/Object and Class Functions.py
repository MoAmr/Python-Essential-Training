# The Python Standard Library includes functions for working on classes and objects.


a = 42
# type function operates on an object and returns the class of that object or the type of that object.
b = type(a)
c = isinstance(a, int)
# id prints the number that represents a unique number for that particular object.
# And so if you have the same object, the numbers will be the same. And if you have two different objects,
# the numbers will be different.
d = id(a)
e = id(a)
print(a)
print(b)
print(c)
print(d)
print(e)
