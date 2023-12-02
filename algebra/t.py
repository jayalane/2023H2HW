
import math

for i in range(0, 50):
    print ((i * i * i * i + 2 * i * i * i + 3 * i * i + 2 * i) / 8)


def isprime(x):
    for i in range(2, round(math.sqrt(x))):
        if x % i == 0:
            return False
        else:
            return True


for n in range(1, 10):
    for p in range(2, 100):
        if isprime(p):
            print (n, p, (n ** p + (p - 1) * n) / p)
