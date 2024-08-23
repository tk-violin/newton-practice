import numpy as np
import pandas as pd


def f(x):
    return x**2


def deriv(func, x):
    e = pow(10, -6)
    return (func(x + e) - func(x)) / e


def sec_deriv(func, x):
    e = pow(10, -6)
    return (deriv(func, x + e) - deriv(func, x)) / e


def optimize(func, x_min, x_max, nloop):
    """
    Function for finding possible extreme values within (and near)
    the designated range of x (x_min ~ x_max).
    It repeats Newton's Method for "nloop" times and
    print x, f(x), and probability density of x

    Inputs:
    x_min, x_max: range of finding extremums.
     (Note: outrange extremums may be found.)
    nloop: number of loops
    """

    n = 0
    x_list = []
    fx_list = []
    e = pow(10, -6)
    errcount = 0
    err = 0
    while n < nloop:
        new = x_min + (x_max - x_min) * np.random.rand()
        preb = x_min + (x_max - x_min) * np.random.rand()
        while abs(new - preb) > e:
            try:
                preb = new
                first_order = deriv(func, new)
                second_order = sec_deriv(func, new)
                new = preb - first_order / second_order
            except ZeroDivisionError:
                err = 1
                errcount += 1
                break

        if err == 0:
            x_list.append(round(new, 6))
            fx_list.append(round(func(new), 6))
            n += 1
        elif errcount > nloop:
            print("Problem occurs. It is hard to find convergence")
            return
        else:
            err = 0

    print("calculation completed")

    ans_dic = {}

    for i in range(len(x_list)):
        temp = x_list[i]
        if temp not in ans_dic:
            ans_dic[temp] = [fx_list[i], 1]
        else:
            ans_dic[temp][1] += 1

    ans_df = pd.DataFrame(columns=["x", "fx", "density"])

    for mykey, myvalue in ans_dic.items():
        ans_df.loc[str(mykey)] = [mykey, myvalue[0], myvalue[1]]

    ans_df = ans_df.sort_values("density", ascending=False)
    ans_df["density"] = ans_df["density"] / sum(ans_df["density"])
    ans_sum = 0
    ans_count = 0

    while ans_sum < 0.8:
        ans_sum += ans_df.iloc[ans_count, 2]
        ans_count += 1

    ans_df2 = ans_df[:ans_count]
    ans_df2 = ans_df2.sort_values("fx")

    for i in range(ans_df2.shape[0]):
        print(
            "x: ",
            ans_df2.iloc[i, 0],
            "  f(x): ",
            ans_df2.iloc[i, 1],
            "  density: ",
            round(ans_df2.iloc[i, 2] * 100, 3),
            "%",
        )

    return ans_df2


ans1 = optimize(f, -10, 10, 10000)
ans2 = optimize(np.sin, -10, 10, 10000)


def g(x):
    return x


and3 = optimize(g, -10, 10, 10000)
