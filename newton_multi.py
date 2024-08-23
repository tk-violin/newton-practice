import numpy as np
import pandas as pd
import copy

# import scipy.optimize import approx_optimize

def f(x):
    return x[0]**2 + x[1]**2


def deriv(func, x):
    e = pow(10, -6)
    ans = []
    for i in range(len(x)):
        x_new = x + [0] * len(x)
        x_new[i] = x_new[i] + e
        ans.append((func(x_new) - func(x)) / e)
    return ans


def sec_deriv(func, x):
    e = pow(10, -6)
    ans = []
    for i in range(len(x)):
        x_new = x + [0] * len(x)
        x_new[i] = x_new[i] + e
        tempans = []
        ans_new = deriv(func, x_new) 
        ans_old = deriv(func, x)
        for j in range(len(x)):
            tempans.append((ans_new[j] - ans_old[j]) / e)
        ans.append(tempans)
    return ans


def absol(x):
    ans = 0
    for i in x:
        ans += pow(i, 2)
    return pow(ans, 1/2)


def optimize(func, primer):
    e = pow(10, -6)
    new = list(primer)
    preb = new + [0] * len(primer)
    preb[0] = preb[0] - 1
    while abs(absol(new) - absol(preb)) > e:
        preb = list(new)
        first_order = deriv(func, new)
        second_order = np.linalg.inv(sec_deriv(func, new))
        new = preb - np.dot(second_order, first_order)
    return [func(new), new]


optimize(f, [1,2])