
def hailstone(n):
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n//2)
    if n % 2 == 1:
        return 1 + hailstone(n*3+1)

hailstone(5)

