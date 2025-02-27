def find_digit(k):
    assert k > 0

    def f(x):
        assert x > 0
        count = 1
        while count < k and x > 0:
            x = x // 10
            count += 1

        if x > 0:
            return x % 10
        else:
            return 0

    return f

"""官方解法"""
def find_digit(k):
    assert k > 0
    def f(x):
       return x // pow(10,k-1) % 10 #得到第k位数字
    return f
