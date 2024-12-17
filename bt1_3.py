from typing import List

def sum_factors(N: int) -> List[int]:
    factors_ = []
    for i in range(1, N // 2 + 1):
        if N % i == 0:
            factors_.append(i)
    return sum(factors_)



if __name__ == '__main__':
    N = int(input("Enter a positive number: "))
    sum_factors_ = sum_factors(N)
    print(f'Summary of factors: {sum_factors_}')
