# types and ids in Python

x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print('y is {}'.format(y))
print(type(x))
print(type(y))
print(id(x[0]))
print(id(y[0]))

# use is operator if you want to check if two objects are of the type
if x[0] is y[0]:
    print('yep')
else:
    print('nope')

if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('nope')
