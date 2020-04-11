# The Python standard library provides a number of useful string-oriented functions
# beyond the methods of the string class itself.


class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is {self._n} 💀'

    def __str__(self):
        return f'str: the number of bunnies is {self._n}'


x = bunny(47)
# repr stands for representation. It'll print the best possible string representation of an object.
# If you do have the string version, it'll default to the string version. If you don't have the string version,
# it will default to the repr version.
print(repr(x))
print(x)
# ascii function, which makes sure that that representation is only ASCII characters.
print(ascii(x))
# chr function - prints the character represented by that Unicode position.
print(chr(128128))
# ord function - gets the unicode number of character
print(ord('💀'))
