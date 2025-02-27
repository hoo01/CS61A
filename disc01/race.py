def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        """minites == 0 防止初始状态 tortoise == hare == 0 时直接退出，这是在保证第一轮循环时为True,
        当乌龟和兔子距离不同（不论谁领先），继续循环，直到它们走过的距离相等"""
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes