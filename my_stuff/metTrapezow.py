

def calka(fun, a, b):
    dx = (b - a) / 99
    Int = 0
    for i in range(100):
        Int += (fun(i*dx) + fun((i+1)*dx))/2*dx
        return Int

def x_kwadrat(x):
    return x**2


print("Calka =", calka(x_kwadrat, 0., 10.))
