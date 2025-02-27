def has_digit(n,k):
    """ return whether k is a digit in n.
    >>> has_digit(10,1)
    True
    >>> has_digit(221,3)
    False
    """
    assert k >= 0 and k < 10

    while n > 0:
        last = n % 10
        n = n // 10
        if last == k:
            return True
    return False

def count_uni_digit(n):
    count = 0
    i = 0
    while i < 10:
        if has_digit(n,i):
            count += 1
        i += 1
    return count

#另一种解法
def unique_digit(n):
    unique = 0
    while n > 0:
        last = n % 10
        n = n // 10
        if not has_digit(n,last):
            unique += 1
    return unique