import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2!= 0:
        raise ValueError("The number of coefficients must be even")
    if xs[-1] == 0:
        raise ValueError("The largest coefficient must be non-zero")
    if len(xs) == 2:
        return -xs[0] / xs[1]
    else:
        a, b, c = xs[-1], xs[-2], xs[-3]
        D = b**2 - 4*a*c
        if D < 0:
            raise ValueError("No real solution")
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        if poly(xs, x1) == 0:
            return x1
        else:
            return x2