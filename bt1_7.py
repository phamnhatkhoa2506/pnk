import math

from typing import List

def sieve(N: int) -> List[int]:
    primes = [True] * (N + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(math.sqrt(N)) + 1):
        if primes[i]:
            for j in range(i*i, N + 1, i):
                primes[j] = False

    return primes

if __name__ == '__main__':
    N = int(input("Enter a positive number: "))
    primes = sieve(N)