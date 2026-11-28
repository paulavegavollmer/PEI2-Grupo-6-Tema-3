#polinomios lagrange
def lagrange(x, y, xi):
    n = len(x)
    L = 0
    for i in range(n):
        li = 1
        for j in range(n):
            if i != j:
                li *= (xi - x[j]) / (x[i] - x[j])
        L += y[i] * li
    return L