![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113006.png)

![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113018.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113027.png)
generalize后，见gene_area.py：
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113048.png)
assert 是 Python 中的一个内置语句，用于断言某个条件是否为真。如果条件为真（即表达式的值为 True），程序会继续执行；如果条件为假（即表达式的值为 False），程序会抛出一个 AssertionError 异常，并终止执行。

**第二个例子 三次幂：**
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113121.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113129.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113140.png)
**第三个例子-functions as return values**
`def make_adder(n):`
    `"""return a function that takes one argument and return k+n.`
    `>>> add_three = make_adder(3)`
    `>>> add_three(4)`
    `7`
    `"""`
    `def adder(k):`
        `return k + n`
    `return adder #返回的是adder函数，而不是adder函数执行的结果`

docstring部分的解释：

当你执行 add_three = make_adder(3) 时，实际上是创建了一个新的 adder(k) 函数，并且在这个新函数中，n 的值已经被固定为 3。这种机制叫做闭包。

n 的值已经“绑定”到 adder(k) 函数中了，这意味着 add_three 这个新函数永远记住了 n = 3 这个值。
因此，当你调用 add_three(4) 时，实际上是在调用 adder(k) 函数，其中 k 被传递为 4，而 n 永远是 3，所以返回的是 4 + 3 = 7。


2.调用 add_three(4)：
现在，add_three 是一个函数，实际上它就是 adder 函数的引用。我们调用 add_three(4)，这时 adder(4) 被执行了，具体步骤如下：

	• adder(k) 中，k 被传入了 4，并且 n 在闭包中被记住了是 3（因为在创建 add_three 时 make_adder(3) 传入了 n=3）。
	• 因此，adder(4) 计算的是 4 + 3，返回值是 7。
所以 add_three(4) 返回的是 7。

证明了函数是第一类值，意味着它们可以作为参数传递，可以作为返回值返回
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228113324.png)
