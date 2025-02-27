def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_test(n=None):
    # 如果传入了 n，就执行自定义的测试，否则运行默认的测试
    if n is None:
        assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
        assert fib(3) == 2, 'The 3rd Fibonacci number should be 2'
        assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
    else:
        print(f'testing fib({n})')
        print(f'fib({n}) =', fib(n))



