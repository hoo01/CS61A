函数的定义中
	• def关键字，可以定义带有名称的函数
	• lambda关键字，可以定义匿名函数（无名称）
	• 有名称的函数，可以基于名称重复使用。
	• 无名称的匿名函数，只可临时使用一次。
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228114606.png)
![Uploading file...nzwu4]()
带有名称的函数：
- 通过def关键字，定义一个函数，并传入，如下图：
-![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228114636.png)
- 也可以通过lambda关键字，传入一个一次性使用的lambda匿名函数
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228114659.png)
使用def和使用lambda，定义的函数功能完全一致，只是lambda关键字定义的函数是匿名的，无法二次使用

• Lambda expressions can be used as an operator or operand
	`negate = lambda f, x: -f(x)`
	`negate(lambda x: x * x, 3)`
	来自 <https://www.learncs.site/docs/curriculum-resource/cs61a/lab/lab02#higher-order-functions> 
	• 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
	• 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
	
	`f = lambda x:x*x`
	`print(f(5))`
	
	同样，也可以把匿名函数作为返回值返回，比如：
	`def build(x, y):`
    `return lambda: x * x + y * y`