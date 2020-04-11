# The Python Standard Library includes a wide selection of modules available for
# your use in a standard Python installation.


import sys
import os
import random
import datetime


def main():
    v = sys.version_info
    p = sys.platform
    o = os.name
    env = os.getenv('PATH')
    current_working_dir = os.getcwd()
    random_num = os.urandom(25).hex()
    random_num1 = random.randint(1, 1000)
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    microsecond = now.microsecond
    print('Python version {}.{}.{}'.format(*v))
    print(f'Platform is {p}')
    print(f'Operating System is {o}')
    print(f'My PATH: {env}')
    print(f'My Current Working Directory: {current_working_dir}')
    print(f'Generated Random Number: {random_num}')
    print(f'Generated Random Number: {random_num1}')
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    print(f'String Representation for date time: {now}')
    print(f'Current year: {year}')
    print(f'Current month: {month}')
    print(f'Current day: {day}')
    print(f'Current hour: {hour}')
    print(f'Current minute: {minute}')
    print(f'Current second: {second}')
    print(f'Current microsecond: {microsecond}')


if __name__ == '__main__': main()
