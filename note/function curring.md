![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228151701.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228151708.png)
结构分析
	1. 最外层的 lambda f::
		- 这是定义了一个接受参数 f 的匿名函数。这个函数的作用是接收一个函数 f 作为输入，返回一个新的函数，这个新函数会继续接收参数。
	2. 中间的 lambda x::
		- 在 lambda f: 返回的函数中，lambda x: 定义了一个接受单一参数 x 的匿名函数。并返回一个函数，这个新函数依赖传入的x值。
	3. 最内层的 lambda y::
		 - 最内层的 lambda y: 定义了一个接受单一参数 y 的匿名函数。这个函数的目的是在外层函数已经提供了 x 的值后，再接收 y 作为参数。
	4. 定义的顺序非常重要！必须是先传入f,再传入x,再传入y 详见lab02-Q3
	curry2(f)(x)(y)  # 正确！
	curry2(x)(f)(y) # ❌ 不符合结构 
	curry2(2) # ❌ 2 不是函数



每一层的 lambda 是返回了一个新的函数，且每一层都依赖于外层传入的值。
lambda 嵌套求值时，先计算内部，再计算外部！

思考：
result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)