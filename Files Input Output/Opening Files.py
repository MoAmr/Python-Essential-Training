# Python provides the open function for opening files.


def main():
    # Open function here, by default, it opens the file in read-only mode, which would be the same as providing
    # a mode with a R letter.
    f = open('lines.txt', 'r')
    for line in f:
        # Obviously each of the lines is returned as a string, and the string class has an R-strip method,
        # which will strip any white space, including new lines, from the end of the line. And this allows us to print
        # them or to do whatever with them without having to worry about dealing with the line endings.
        print(line.rstrip())


if __name__ == '__main__': main()
