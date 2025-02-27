def match_k(k):
    assert k > 0

    def f(x):
        assert x > 0

        while x // pow(10,k) > 0: # 只要 x 还有 k 位以上
            last = x % 10 #取最右边的数字
            kth_last = (x // pow(10,k)) % 10#取相隔k位的数字

            if last != kth_last:
                return False

            x = x // 10#去掉最低位，继续比较
        return True
    return f
