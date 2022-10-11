from cmath import sqrt
from random import randint

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

def convertDecimalToBinary(n):
    binaries = []
    while n != 0:
        remainder = n % 2
        binaries.append(remainder)
        n = n // 2
    binaries.reverse()
    return binaries

def mod(base, exponent, modulo):
    binaries = convertDecimalToBinary(exponent)
    length = len(binaries)
    remainders = []
    remainders.append(base % modulo)
    for i in range(1, length):
        r = pow(remainders[i - 1], 2) % modulo
        remainders.append(r)
    result = 1
    for i in range(0, length):
        bit = binaries[length - 1 - i]
        if bit == 0:
            continue
        result = result * remainders[i] % modulo
    return result

def toDecimal(str):
    s = str.encode('utf-8')
    n = int(s.hex(), 16)
    return n

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
    
    def encrypt(self, msg, chunkSize = 3):
        splittedMsg = [msg[i:i+chunkSize] for i in range(0, len(msg), chunkSize)]
        decimalMsg = list(map(toDecimal, splittedMsg))
        result = []
        for m in decimalMsg:
            cipher = mod(m, self.e, self.N)
            result.append(cipher)
        return result

rsa = RSAResolver()
rsa.encrypt("Hello World")
