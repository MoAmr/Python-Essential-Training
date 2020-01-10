# functions in Python

def function(n=1):
    print(n)
    return n * 2


x = function(100)
print(x)


# prime function
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


# list of primes function
def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=' ', flush=True)
    print()


list_primes()

# n = 6
# if isprime(n):
#     print(f'{n} is prime')
# else:
#     print(f'{n} is not prime')
