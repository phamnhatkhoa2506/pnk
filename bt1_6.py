import math

def aproximate_number_of_prime(N: int) -> int:
    return int(N / math.log(N))

if __name__ == '__main__':
    N = int(input("Enter a positive number: "))
    print("Aproximate Number of primes: ", aproximate_number_of_prime(N))