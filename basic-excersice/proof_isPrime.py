# to proof that integer n the value of n^2 + n + 41 is a prime number

import math

def isPrime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print("integer n the value of n^2 + n + 41 is prime")

n = int(input())
result = int(math.pow(n, 2) + n + 41)

if isPrime(result):
    print(f"{result} is a prime number")
else:
    print(f"{result} is not a prime number")
