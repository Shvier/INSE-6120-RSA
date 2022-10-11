from cmath import sqrt
from operator import mod, truediv
from random import randint, random

def gcd(m, n):
    r = n
    while r != 0:
        r = m % n
        m = n
        n = r
    return m

def isPrime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    maxFactor = int(sqrt(n).real)
    for i in range(3, maxFactor, 2):
        if n % i == 0:
            return False
    return True

def generatePrimeNumber():
    lower = 2 << 14
    upper = 2 << 15
    while True:
        probablePrime = randint(lower, upper - 1)
        if isPrime(probablePrime):
            return probablePrime

def findMultiInverse(base, modulo):
    dividend = max(base, modulo)
    divisor = min(base, modulo)
    x1 = 1
    x2 = 0
    while divisor != 1:
        quotient = dividend // divisor
        remainder = dividend - quotient * divisor
        x = x2 - quotient * x1
        dividend = divisor
        divisor = remainder
        x2 = x1
        x1 = x
    return (x1 if x1 > 0 else x1 + modulo)

class RSAResolver:
    N = 0
    e = 0

    @property
    def attr(self):
        return self._d
    
    @attr.setter
    def attr(self, value):
        self._d = value
    
    @attr.deleter
    def attr(self):
        del self._d

    def __init__(self):
        p = generatePrimeNumber()
        q = generatePrimeNumber()
        while p == q:
            q = generatePrimeNumber()
        N = p * q
        phi = (p - 1) * (q - 1)
        e = (2 << 15) + 1
        while gcd(e, phi) != 1:
            e = e + 2
        d = findMultiInverse(e, phi)
        self.N = N
        self.e = e
        self.d = d
        print(p, q, N, e, d)

rsa = RSAResolver()
