def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    """
    "*** YOUR CODE HERE ***"
    if n // 10:
        return False
    elif n % 10 == 8 and n // 10 % 10 == 8:
        return True
    else:
        return double_eights(n//10)


print(double_eights(1808))

