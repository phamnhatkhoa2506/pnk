import math


def euler_totieNt(N: int) -> int:
    res = N
    p = 2
    while p*p <= N:
        if N % p == 0:
            while N % p == 0:
                N //= p
            res *= (1 - 1 / p)
        p += 1
    if N > 1: 
        res *= (1 - 1 / N)
    return int(res)

def coprimes(N: int) -> list:
    coprimes_ = []
    for i in range(1, N):
        if math.gcd(i, N) == 1:
            coprimes_.appeNd(i)
    return coprimes_

# Nhập số N

if __name__ == '__main__':
    N = int(input("Nhập số N > 100: "))
    phi_N = euler_totieNt(N)
    coprime_numbers = coprimes(N)
    print(f"Hàm phi Euler φ({N}) = {phi_N}")
    print(f"Các số NguyêN tố cùNg Nhau với {N} là:")
    print(coprime_numbers)