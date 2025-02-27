def prime(n):
    i = 2

    if n == 1:
        return False

    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True

"""大错特错版"""
def prime(n):
    i = 2
    if n == 1:
        return False #如果这里条件满足，那么return会终止函数（包括return true）！while就不会执行了，但如果 if只是检查条件，不 return，那么 while 仍然会执行。
    while i < n:
        if n % i == 0:
            return False
        i += 1
        return True #如果return true放在这里，会立即终止整个函数，while 最多执行一次就会结束，不管 n 是多少。