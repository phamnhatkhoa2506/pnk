from functools import reduce
from typing import List

def mod_inverse(a: List[int], 
                m: List[int]) -> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def chinese_remainder_theorem(a: List[int], 
                              n: List[int]) -> int:
    N = reduce(lambda x, y: x * y, n) 
    x = 0
    for a_i, n_i in zip(a, n):
        N_i = N // n_i
        M_i = mod_inverse(N_i, n_i)
        x += a_i * N_i * M_i
    return x % N

if __name__ == '__main__':
    
    a = [2, 3, 2]  
    n = [3, 5, 7]  
   
    result = chinese_remainder_theorem(a, n)
    print(f"Nghiệm x là: {result}")
