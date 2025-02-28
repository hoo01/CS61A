cascade recursion
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152749.png)
调用栈中的结构
每一次调用 cascade 函数时，Python 都会为该调用分配一个新的 栈帧 (frame)。栈帧会保存：
	1. 当前调用的参数（比如 n 的值）。
	2. 函数内的局部变量。
	3. 当前执行到的代码位置。
当递归调用完成时，当前栈帧被销毁，并将控制权交还给上一个栈帧，继续执行未完成的代码。

当前状态
	1. 调用栈显示了 3 个栈帧：
		- f1 是最外层调用 cascade(123)。
		- f2 是第二层调用 cascade(12)。
		- f3 是最内层调用 cascade(1)。
	2. 在 f3 中：
		- n = 1，符合基本情况 (n < 10)。
		- 打印 1。
		- 然后返回 None，这意味着 f3 完成了任务，被销毁。
回溯到上一层（f2）
	1. 回到 f2 的调用栈（n = 12），此时 cascade(n // 10) 的调用已经完成（刚刚处理完 n = 1 的情况）。
	2. 挂起的代码继续执行：

print(n)  # 这是 cascade(12) 递归调用后的部分
	n = 12，所以此时打印 12。
	
为什么会回到 print(12)？
	这是因为在递归调用时，cascade(12) 调用了 cascade(1)，并将控制权暂时交给了 cascade(1)。当 cascade(1) 执行完毕返回后，cascade(12) 会继续执行它的剩余代码：
		1. cascade(1) 返回后，cascade(12) 的递归调用部分完成。
		2. 剩下的 print(n) 还没有被执行，所以回溯到这里，打印 12。

一道很好的打印类题目
```python
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)
```


grow = lambda n:f_then_g(grow,print,n//10)
shrink = lambda n:f_then_g(print,shrink,n//10)

inverse_cascade(123)
