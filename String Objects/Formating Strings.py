# Python has rich string formatting capabilities.


x = 42 * 747 * 1000
y = 73
z = 42
# {} is placeholder
# Python 2
print('the numbers are {0:<5} {1:+05}'.format(x, y))
print('the number is {:,}'.format(x))
print('the number is {:f}'.format(x))
print('the number is {:3f}'.format(x))
print('the number is {:,}'.format(x).replace(',', '. '))
print('the number is {:o}'.format(z))
print('the number is {:b}'.format(z))
print('the number is {:x}'.format(z))

# Python 3
# Using f Strings instead of format()
print(f'the number is {z:.3f}')




