import math

from typing import List, Sequence

def split(A: Sequence[List[int]]) -> Sequence[List[float]]:
    L = [[0]*len(A) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(i + 1):
            if i == j:
                L[i][i] = math.sqrt(
                    A[i][i] - sum([L[i][k]**2 for k in range(i)])
                )
            elif i > j:
                L[i][j] = (
                    A[i][j] - sum([L[i][k]*L[j][k] for k in range(j)])
                ) / L[j][j]

    return L

if __name__ == '__main__':
    A = [
        [4, 12, -16],
        [12, 37, -43],
        [-16, -43, 98]
    ]

    print(split(A))

