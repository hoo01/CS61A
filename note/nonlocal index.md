内部嵌套的函数加nonlocal index表明是修改外部作用域（非全局）的Index变量，如果不使用 nonlocal，会遇到以下问题：
index = (index + 1) % len(outcomes) 会创建一个新的局部变量 index，这会导致外部的 index 不会被更新，循环过程中的 index 会在每次调用时被重置，结果就是 dice() 每次都会返回相同的值，而不会按顺序循环。
