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

def convertStrToDecimal(str):
    s = str.encode('utf-8')
    n = int(s.hex(), 16)
    return n

def convertDecimaltoStr(n):
    hexMsg = f'{n:x}'
    return bytearray.fromhex(hexMsg).decode()
    