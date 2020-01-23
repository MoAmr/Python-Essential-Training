# Sequence Types in Python.
# tuple is an immutable type array
# range is immutable type
# Dictionary is a mutable searchable sequence of key value pairs
x = (1, 2, 3, 4, 5)
# x[2] = 42
for a in x:
    print('a is {}'.format(a))

y = list(range(5, 50, 5))
y[2] = 42
for b in y:
    print('b is {}'.format(b))

z = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
z['three'] = 42
for k, v in z.items():
    print('k: {}, v: {}'.format(k, v))
