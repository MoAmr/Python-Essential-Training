# loops in Python

words = ['one', 'two', 'three', 'four', 'five']

# while loop
n = 0
while n < 5:
    print(words[n])
    n += 1

# Simple Fibonacci Series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a + b

print()  # line ending

# for loop

for i in words:
    print(i)
