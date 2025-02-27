from operator import floordiv,mod
#d=10不是传参，只是占位符，意味着如果没有输入第二个参数，那么d=10
def divide_exact(n,d=10):
    """
    return the quotient and remainder of dividing N by D.
    >>> q,r = divide_exact(2013,10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n,d),mod(n,d)

q,r = divide_exact(2013)
print('quotient:',q)
print('remainder:',r)

from doctest import run_docstring_examples
run_docstring_examples(divide_exact,globals(),True)

