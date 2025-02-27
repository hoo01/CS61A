def sevens(n,k):
    assert type(n) == int and type(k) == int, "n and k must be integers"
    assert n >= 1 and k >= 1, "n and k must be greater than or equal to 1"

    def has_seven(i):
        if i == 7:
            return True
        if i // 10 > 0:
            return has_seven(i//10)
        return False

    def recursive(i,who,direction):
        if i == n:
            return who
        if has_seven(i):
            direction = -direction
        who = (who + direction - 1) % k + 1

        return recursive(i+1,who,direction)
    
    return recursive(1,1,1)