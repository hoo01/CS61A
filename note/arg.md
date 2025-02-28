*arg
def make_test_dice(*outcomes):
加*可以传递任意数量的参数，甚至可以不传递任何参数，并将它们打包成一个元组。

比如：
`def printed(f):`
    `def print_and_return(*args):  # 接受任意数量的参数`
        `result = f(*args)  # 将这些参数传递给目标函数 f`
        `print('Result:', result)  # 打印结果`
        `return result  # 返回结果`
    `return print_and_return  # 返回包装函数`

# 使用示例
printed_pow = printed(pow)  # 将 pow 函数传递给 printed 函数
printed_pow(2, 8)  # 调用 pow(2, 8)


再如：
def make_test_dice(*outcomes):
    """Return a dice function that cycles through the outcomes."""
    
    def dice():
        outcome = outcomes[0]  # 获取当前结果的第一个骰子值
        outcomes = outcomes[1:] + [outcome]  # 将第一个结果移到末尾，形成循环
        return outcome  # 返回当前的骰子结果
    
    return dice  # 返回骰子函数

参考题目见hog project problem8