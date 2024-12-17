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


def to_prime_factors(N: int,
                     primes: List[int]) -> str:
    factors = []
    exps = []
    i = 2

    while N > 1:
        if primes[i] and N % i == 0:
            factors.append(i)
            j = 0
            while N % i == 0:
                j += 1
                N /= i

            exps.append(j)
        i += 1

    res = [f'{factor}^{exp}' for factor, exp in zip(factors, exps)]

    return ' * '.join(res)



if __name__ == '__main__':
    N = int(input("Enter a positive number: "))
    primes = sieve(N)
    print(f'After analysting to prime factor: {to_prime_factors(N = N, primes = primes)}')
