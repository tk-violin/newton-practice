def f(x):
    return x ** 2 + 2 * x + 1

def deriv(func, x):
    e = pow(10, -6)
    return (func(x + e) - func(x)) / e

def sec_deriv(func, x):
    e = pow(10, -6)
    return (deriv(func, x + e) - deriv(func, x)) / e

def newton(func):
    new = 0
    preb = 100
    p = pow(10, -6)
    while abs(new - preb) > p:
        preb = new
        first_order = deriv(func, new)
        second_order = sec_deriv(func, new)
        new = preb - first_order / second_order
    return new

newton(f)