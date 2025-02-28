![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228111806.png)
fibonacci左右对比，右更好
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228111845.png)
can if statement convert to if function?
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228111902.png)
error's reason:
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228111913.png)
when we replace the conditional statement with a call expression, we had a different 
evaluation rule
在评估这个过程中，我们先确定我们要调用的函数以及我们在执行主体之前调用它的所有三个参数。For evaluating this, we figure out what function we're going to call and allthree arguments that we're calling it on before we ever execute the body.
在我们讨论0或者其他内容之前，由于对负数进行了平方根运算，我们就遇到了一个错误。And before we ever got to the 0 or got to this, we reached an error because the square root of a negative number was taken
call expression don't allow you to skip evualting parts of the call expression,
all the parts are always evaluated before the function is called

这与控制语句不同，控制语句实际上会选择执行语句的哪些部分以及跳过哪些部分。And that's different from control statements, which actually pick which parts of the statement are executed and which parts are skipped.

举例：
调用表达式（Call Expression） 中的所有部分（例如参数）都会在函数被调用之前被计算。
这意味着所有的参数都会被计算出来，无论这些参数是否会在函数内部使用。
示例：包含副作用（Side Effects）

```python
 def print_value(x):
    print(f"Value: {x}")
    return x

result = print_value(3 + 2)  # 这里 3 + 2 会先被计算，输出 "Value: 5"```
在这个例子中,虽然函数 print_value 只是打印出参数 x，但 3 + 2 仍然会在函数调用之前被计算，导致副作用发生（即打印出 "Value: 5"）。