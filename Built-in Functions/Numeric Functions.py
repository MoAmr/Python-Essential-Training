# The Python Standard Library provides a rich set of built-in functions for working with numbers.


x = '47'
a = -47
b = 47
# I'm using the int function and it's actually not a function
# it's a constructor for the int type and it'll return an int from another type.
# We're converting a string to an int by calling the int function which is actually the int constructor.
y = int(x)
y = float(x)
z = abs(a)
# Function divmod returns both the quotient and the remainder in a tuple of a division.
z1 = divmod(b, 3)
# The complex function is a type constructor. Complex numbers are two-dimensional numbers.
# Python uses j instead of i for the imaginary part of the number.
z2 = complex(b, 73)
print(f'x is {type(x)}')
print(f'x is {x}')
print(f'a is {a}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(f'z is {z}')
print(f'z1 is {z1}')
print(f'z2 is {z2}')
