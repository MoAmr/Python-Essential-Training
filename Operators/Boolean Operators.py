# Boolean Operators in Python.

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if y in x:
    print('expression is true')
if 'tree' in x:
    print('expression is true')
if y is x[0]:
    print('expression is true')
if y is not x[1]:
    print('expression is true')
else:
    print('expression is false')
