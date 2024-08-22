def f(x):
    return x**2 + 2 * x + 1  #Just example. You can


def deriv(func, x):
    """
    This function takes first-order derivative.
    e = scalar (significantly small number)
    """
    e = pow(10, -6)
    return (func(x + e) - func(x)) / e


def sec_deriv(func, x):
    """
    This function takes second-order derivative.
    e = scalar (significantly small number)
    """
    e = pow(10, -6)   # significantly 
    return (deriv(func, x + e) - deriv(func, x)) / e


def newton(func):
    """
    This function estimates x to minimize f(x) defined above using Newton method.
    new = new x candidate (0 is the primer.)
    preb = prebious x candidate (100 is the primer.)
    p = scalar (significantly small number)
    once the difference between new and preb reaches smaller than p, the cycle ends. 
    """
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
