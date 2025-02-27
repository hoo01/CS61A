#pow(x,y)返回x的y次幂，即x**y
def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n,term):
    """sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    #计算前n项的和，term一个函数（例如cube）,用于计算序列的每一项

    total,k=0,1
    while k<=n:
        total, k = total + term(k),k+1
    return total

def sum_naturals(n):
    """sum the first n natural numbers.
    >>> sum_naturals(5)
    15
    """
    return summation(n,identity)

def sum_cubes(n):
    """sum the first n cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    return summation(n,cube)