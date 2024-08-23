import numpy as np
import pandas as pd

def f(x):
    return x ** 2

def deriv(func, x):
    e = pow(10, -6)
    return (func(x + e) - func(x)) / e

def sec_deriv(func, x):
    e = pow(10, -6)
    return (deriv(func, x + e) - deriv(func, x)) / e

def optimize(func, x_min, x_max, nloop):
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
            except:
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
    
    data = {'x': x_list, 'fx': fx_list}
    ans_data = {'x': [], 'fx': [], 'density':[]}
    df = pd.DataFrame.from_dict(data)
    ans_df = pd.DataFrame.from_dict(ans_data)
    
    for i in range(df.shape[0]):
        temp = df.iloc[i, 0]
        if df.iloc[i, 0] in list(ans_df['x']):
            ans_df.loc[ans_df['x'] == temp, "density"] += 1
        else:
            ans_df.loc[str(temp)] = [df.iloc[i, 0], df.iloc[i, 1], 1]

    ans_df = ans_df.sort_values('density', ascending = False)
    ans_df['density'] = ans_df['density'] / sum(ans_df['density']) 

    ans_sum = 0
    ans_count = 0

    while ans_sum < 0.8:
        ans_sum += ans_df.iloc[ans_count, 2]
        ans_count += 1
    
    ans_df2 = ans_df[:ans_count]
    ans_df2 = ans_df2.sort_values('fx')

    for i in range(ans_df2.shape[0]):
        print("x: ", ans_df2.iloc[i, 0],
              "  f(x): ", ans_df2.iloc[i, 1],
              "  density: ", round(ans_df2.iloc[i, 2] * 100, 3), "%"
        )
        
    return ans_df2


optimize(f, -10, 10, 10000)
optimize(np.sin, -10, 10, 10000)

def g(x):
    return x
    
optimize(g, -10, 10, 10000)