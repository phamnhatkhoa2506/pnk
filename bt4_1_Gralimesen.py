def f(x: float) -> float:
    return x**2 - 4*x + 4

def f_derivative(x: float) -> float:
    return 2*x - 4

def gradient_descent(x0: float,
                     alpha: float = .1,
                     epsilon: float = 1e-6,
                     n: int = 100) -> float:
    x = x0
    for _ in range(n):
        grad = f_derivative(x)
        x_new = x - alpha * grad
        
        if abs(x_new - x) < epsilon:
            return x_new 
        x = x_new
    
    return x 

if __name__ == '__main__':
    x0 = 0  
    x_min = gradient_descent(x0)
    print(f"Giá trị nhỏ nhất của hàm là: {f(x_min)} tại x = {x_min}")