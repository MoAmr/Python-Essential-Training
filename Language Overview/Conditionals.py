# Conditionals
# Note that Python does not have switch or case statements.
x = 15
y = 20

if x < y:
    print('x < y: x is {} y is {}'.format(x, y))
elif x > y:
    print('x > y: x is {} y is {}'.format(x, y))
elif x == y:
    print('x == y: x is {} y is {}'.format(x, y))
else:
    print('do something else.')
