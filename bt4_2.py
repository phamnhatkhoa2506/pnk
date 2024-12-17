import sympy as sp

if __name__ == '__main__':
    x, y, lamb = sp.symbols('x y lambda')

    f = x**2 + y**2
    g = x + y - 1
    L = f - lamb * g

    x_grad = sp.diff(L, x)
    y_grad = sp.diff(L, y)
    lambda_grad = sp.diff(L, lamb)

    solutions = sp.solve([x_grad, y_grad, lambda_grad], [x, y, lamb])

    print(solutions)
