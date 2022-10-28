from random import randint
import num_theory

class ElGamal:

    @classmethod
    def newPair(self):
        p = num_theory.generatePrimeNumber()
        g = randint(2 << 14, p)
        while num_theory.gcd(g, p) != 1:
            g = randint(2 << 14, p)
        x = randint(2 << 14, p)
        y = num_theory.mod(g, x, p)
        print(f'Public Key is: (y: {y}, g: {g}, p: {p})')
        print(f'Private Key is: {x}')
    
    @classmethod
    def encrypt(self, msg, y, g, p):
        k = randint(1, p)
        r = num_theory.mod(g, k, p)
        c = (num_theory.mod(y, k, p) * msg) % p
        return (r, c)

    @classmethod
    def decrypt(self, r, c, x, p):
        miR = num_theory.findMultiInverse(r, p)
        msg = (num_theory.mod(miR, x, p) * c) % p
        return msg

# elgamal = ElGamal.newPair()
msg = 123
y = 40883
g = 34555
p = 47339
x = 43663
r, c = ElGamal.encrypt(msg, y, g, p)
print(f'cipher is: (r: {r}, c: {c})')
m = ElGamal.decrypt(r, c, x, p)
print(f'message is: {m}')
