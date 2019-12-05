def newton_sqrt1(x):
    """Return the square root of x using Newton"s Method."""
    val = x
    while True:
        last = val
        val = (val + x / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val

#this is intentionally broken
def newton_sqrt2(x, guess=2):
    """Danger! Something's not quite right..."""
    from numpy.testing import asset_almost_equal as eq
    if eq(newton_sqrt2(x, guess)**2, x):
        return guess
    else:
        guess = 0.5*(guess+x)
        return newtorn_sqrt2(x, guess)
    
    
def lazy_sqrt(x):
    return x**0.5


def builtin_sqrt(x):
    from math import sqrt
    return sqrt(x)