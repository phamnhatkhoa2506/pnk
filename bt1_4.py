from typing import List
from functools import reduce

def multiply(a: int,
             b: int) -> int:
    return a*b

def multiply_factors(N: int) -> List[int]:
    factors_ = []
    for i in range(1, N // 2 + 1):
        if N % i == 0:
            factors_.append(i)
    return reduce(multiply, factors_)



if __name__ == '__main__':
    N = int(input("Enter a positive number: "))
    multiply_factors_ = multiply_factors(N)
    print(f'Summary of factors: {multiply_factors_}')
