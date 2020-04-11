# Reading and writing text files is remarkably easy in Python.


def main():
    # Opening it in read mode and in text mode, btw this is the default as open('lines.txt')
    # Python principle that explicit is always better than implicit. so we used open('lines.txt', 'rt')
    infile = open('lines.txt', 'rt')
    # Open this file in write mode, and again specifying the t for text mode even though it is the default.
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        # r strip method to strip the line endings from the file
        # print function with file equals output
        # You may optionally instead of using print to write the file, outfile.writelines(line)
        # you may use the out-file method, write lines, and this will work just as well
        print(line.rstrip(), file=outfile)
        # I print a dot and you notice I have this end equals empty string, and that prevents print from printing
        # a new line after each dot so that they'll just go across the line and make a little progress bar,
        # and this flush equals True, this flushes the output buffer.
        # outfile.writelines(line)
        print('.', end='', flush=True)
    # I close the out file, and this is important because again, buffering, all of what we've written to the file
    # may not be completely written by the time our main function ends, and we want to prevent any data loss,
    # so it's a good idea to close the file explicitly that you've written to.
    outfile.close()
    print('\ndone.')


if __name__ == '__main__': main()