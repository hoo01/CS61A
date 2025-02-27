def sevens(n,k):
    assert type(n) == int and type(k) == int, "n and k must be integers"
    assert n >= 1 and k >= 1, "n and k must be greater than or equal to 1"

    def has_seven(i):
        if i % 7 == 0:
            return True
        while i > 0:  # 只要 x 还有 k 位以上
            last = i % 10  # 取最右边的数字
            if last == 7:
                return True
            i = i // 10  # 去掉最低位，继续比较
        return False

    direction = 1
    i = 1 #起始数字
    who = 1 #起始玩家

    while i < n:
        if has_seven(i):
            direction = -direction
        who = (who + direction - 1) % k + 1
        i += 1

    return who


















