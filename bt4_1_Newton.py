def f(x: float) -> float:
    return x**2 - 4*x + 4

def f_derivative(x: float) -> float:
    return 2*x - 4

def f_double_derivative(x: float) -> float:
    return 2

def newton_method(x0: float,
                  epsilon: float = 1e-6,
                  n: int = 100) -> float:
    x = x0
    for _ in range(n):
        f_prime_val = f_derivative(x)
        f_double_prime_val = f_double_derivative(x)
        
        x_new = x - f_prime_val / f_double_prime_val
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    
    return x  

if __name__ == '__main__':
    x0 = 0 
    x_min = newton_method(x0)

    print(f"Giá trị nhỏ nhất của hàm là: {f(x_min)} tại x = {x_min}")
