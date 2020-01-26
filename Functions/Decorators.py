# Decorators in Python.
# Note: A Decorator is a form of meta programming and can be described as
# a special type of function that returns a wrapper function.

# def f1():
#     print('this is f1')
#
# x = f1
# x()

# here f1 is wrapper of f2
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')

    return f2


@f1
# here f3() function is wrapped inside the decorator function
def f3():
    print('this is f3')


f3()
