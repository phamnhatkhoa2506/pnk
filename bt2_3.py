import numpy as np

def eig(A):
    values, vectors = np.linalg.eig(A)
    return values, vectors

def svd_decomposition(A):
    AtA = np.dot(A.T, A)
    
    eigenvalues, eigenvectors = eig(AtA)
    sigma = np.sqrt(np.abs(eigenvalues))
    V = eigenvectors
    U = np.dot(A, V)

    for i in range(U.shape[1]):
        U[:, i] = U[:, i] / np.linalg.norm(U[:, i])
    
    return U, sigma, V.T

if __name__ == '__main__':
    A = np.array([[3, 2],
                [2, 3]])

    U, sigma, VT = svd_decomposition(A)
    print(U, sigma, VT, sep = '\n')
