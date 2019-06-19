# Module
# A file with a script containing a long python program
# Definitions from other modules can be imported into the main module


def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        print()



def fibo2(n):
    result = []
     a, b = 0,1
    while b < n:
    result.append(b)
    a, b = b, a+b
    return result

# Save the file as fibo.py and import fibo



