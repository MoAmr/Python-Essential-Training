# Python allows you to easily split and join strings based on separator characters.


s = 'This is a long string with a bunch of words in it.'
l = s.split()
# Splitting Strings
print(s.split())
# Splitting on the letter i
print(s.split('i'))
# Joining Strings
s2 = '--'.join(l)
print(s2)