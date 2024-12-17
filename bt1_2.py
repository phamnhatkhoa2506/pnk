from typing import List

def factors(N: int) -> List[int]:
    factors_ = []
    for i in range(1, N // 2 + 1):
        if N % i == 0:
            factors_.append(i)

    return factors_



if __name__ == '__main__':
    N = int(input("Enter a positive number: "))
    factors_ = factors(N)
    print(f'Number of factors: {len(factors_)}')
    print(f'List of factors: {factors_}')
