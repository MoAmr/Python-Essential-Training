# To copy a binary file we use the read and write methods of the file object.


def main():
    # When we open the file, we're opening it with the b now for our file type, as opposed to t for text.
    infile = open('The Grand Egyptian Museum.jpg', 'rb')
    # Likewise, our output file is open for write in binary.
    outfile = open('The Grand Egyptian Museum-copy.jpg', 'wb')
    while True:
        # The first thing we do in the loop is we read a buffer full and you notice I'm using 10 KB as the buffer size.
        # You don't want to read the whole file at once because you don't necessarily know how big the file is and
        # you may not even know how much memory is available for your program. So you want to pick a buffer size that
        # you know is going to be safe.
        # Choose your buffer size carefully, considering the target environment for your code.
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            # Each bar represents 10 KB
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\ndone.')


if __name__ == '__main__': main()
