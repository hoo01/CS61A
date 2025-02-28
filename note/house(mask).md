
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228103743.png)

	• mask = lambda horse: horse(2)
	这里 mask 是一个 lambda 函数，它接收一个参数 horse。
	它的功能是：调用 horse(2)，将 2 作为参数传递给 horse。
	mask 本身只是一个函数，不会直接等于 2 或其他值。
只有调用 mask 时，并且传递一个合适的参数（如另一个函数），才能得到结果。
如果传递的参数是可以调用的函数，例如
def my_function(x):
return x * 2
a = mask(my_function)
结果是a=4


