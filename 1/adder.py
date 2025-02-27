def make_adder(n):
    """return a function that takes one argument and return k+n.
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder #返回的是adder函数，而不是adder函数的结果