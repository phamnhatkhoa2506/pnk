import math

def check_perfect_number_1(N: int) -> bool:
    s = 0
    for i in range(1, N // 2 + 2): 
        s += i
        if s >= N: return False
        
    if s >= N: return False
    return True

def check_perfect_number_2(N: int) -> bool:
    if N % 2 != 0:
        return False
    
    i = 1
    p = 1
    while p <= N:
        if p == N: return True
        i += 1
        p = 2**(i - 1) * (2**i - 1)
    
    return False

if __name__ == '__main__':

    N = int(input("Enter a positive number: "))
    print("Is a perfect number" 
            if check_perfect_number_2(N) 
            else "Not a perfect number")