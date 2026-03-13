# Using math in-built function

# import math as mth

# print(mth.factorial(5))

# Using function

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


print(fact(5))