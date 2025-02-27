def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1
#简化写法：
def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3
def square(x):
    return x * x

def positive(x):
    return max(0, square(x)-100)

def inverse(f):
    """return g(y) sucha that g(f(X)) -> x."""
    return lambda y:search(lambda x:f(x)==y)