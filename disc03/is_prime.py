
def is_prime(n):
    def f(i):
        if n == i:
            return True
        elif n % i == 0:
            return False
        else:
            return f(i+1)
    return f(2)

is_prime(5)