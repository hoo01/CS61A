def swipe(n):
    assert n > 0 and type(n) == int,'Illegal value for n'
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n//10)
        print(n % 10)

swipe(12345)