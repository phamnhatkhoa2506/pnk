import numpy as np

def split(A: np.ndarray) -> tuple[np.ndarray]:
    n = len(A)
    L = np.zeros((n, n))
    U = A.copy()
    P = np.eye(n)
    
    for i in range(n):
        pivot = np.argmax(np.abs(U[i:, i])) + i
        
        U[[i, pivot]] = U[[pivot, i]]
        P[[i, pivot]] = P[[pivot, i]]
        L[[i, pivot]] = L[[pivot, i]]

        L[i, i] = 1
        for j in range(i+1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:] -= L[j, i] * U[i, i:]
    
    return P, L, U

if __name__ == '__main__':

    A = np.array([
        [7, 8, 9],
        [4, 5, 6],
        [0, 2, 3]
    ]).astype(np.float64)

    P, L, U = split(A)

    print("P:", P)
    print("L:", L)
    print("U:", U)