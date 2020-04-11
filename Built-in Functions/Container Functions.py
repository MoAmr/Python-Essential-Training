# The Python standard library provides some useful functions for working with containers.


x = (1, 2, 3, 4, 5)
x1 = (6, 7, 8, 9, 10)
x2 = ('cat', 'dog', 'rabbit', 'velociraptor')
y = (0, 0, 0, 0, 0)
a = x
b = len(x)
c = reversed(x)
for i in c: print(i)
d = list(reversed(x))
e = sum(x)
f = max(x)
g = min(x)
# Boolean values that we can get from functions. Any will give me true if any of these are true. So,
# if I replace these with all zeros, and run it, then I get false, but if I make just one of them a one,
# you'll notice that the result is true.
h = any(x)
i = any(y)
# all function which will return true, only if all of them are true.
j = all(x)
k = all(y)
# you notice we get the zip of these two lists x and x1
l = zip(x, x1)
for counter1, counter2 in l: print(f'{counter1} - {counter2}')
# enumerate gives us two values, an index and a value, this can be useful in getting the order of things.
for c1, c2 in enumerate(x2): print(f'{c1}: {c2}')
print(x)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
