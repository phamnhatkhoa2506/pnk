def gcd(a: int,
        b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a: int,
        b: int) -> int:
    return int(a*b / gcd(a, b))

if __name__ == '__main__':
    a = 2
    b = 4

    print(lcm(a, b))
