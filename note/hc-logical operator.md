logical operator
short-circult evaluation一旦可以确定结果，Python 就不会再计算后续的表达式。

**and**
To evaluate the expression <left> and <right>:
1.Evaluate the subexpression <left>.
2.If the result is a false value v,then the expression evaluates to v.
3.otherwise,the expression evaluates to the value of the subexpression <right>.

To evaluate the expression <left> or <right>:
1.Evaluate the subexpression <left>.
2. If the result is a true value v,then the expression evaluates to v.
3.0therwise,the expression evaluates to the value of the subexpression <right>.
**and 会返回第一个假值，而 or 会返回第一个真值。**

**逻辑与运算符（and）求值规则：**
首先计算左侧表达式（<left>）：
	• 计算左边的子表达式（<left>）。如果它已经是一个假值（如 False、None、0、空字符串等），那么整个 and 表达式的结果就是左侧表达式的值。
	• 如果左侧的结果是一个假值：
	如果左侧的表达式结果是一个假值，那么整个 and 表达式的结果就是左侧表达式的结果。Python 在这种情况下 不会再计算右侧的表达式（<right>），因为无论右侧的表达式是什么，and 运算的结果已经确定了。
	• 否则，返回右侧表达式的值：
如果左侧的表达式不是假值（即它的值被认为是“真”的），那么 Python 会继续计算右侧的表达式，并且返回右侧表达式的值。

		python
		a = 0
		b = 5
		
		result = a and b
		步骤 1：首先计算 a，它的值是 0（假值）。
		步骤 2：由于 a 是假值，整个 and 表达式的结果是 0，不需要再计算右边的 b。
		
		再看一个例子：
		
		python
		a = 10
		b = 5
		
		result = a and b
		步骤 1：首先计算 a，它的值是 10（真值）。
		步骤 2：由于 a 不是假值，继续计算右侧的 b，它的值是 5。
		步骤 3：整个 and 表达式的结果是 b 的值，即 5。


**重点：**
短路求值（Short-circuit evaluation）：当左侧表达式的结果为假值时，Python 会立即返回左侧的结果，而不会去计算右侧的表达式。这样可以提高效率，避免不必要的计算。
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228112417.png)
**逻辑或运算符（or）的求值规则：**
	1. 首先计算左侧表达式（<left>）：
	计算左边的子表达式（<left>）。如果它已经是一个“真”值（例如 True、非零数字、非空字符串等），那么整个 or 表达式的结果就是左侧表达式的值。
	1. 如果左侧的结果是一个真值：
	如果左侧表达式的结果是“真值”，那么 or 表达式的结果就是左侧表达式的值。Python 不会再计算右侧的表达式（<right>），因为无论右侧的表达式是什么，or 运算的结果已经确定了。
	1. 否则，返回右侧表达式的值：
	如果左侧的表达式是“假值”（如 False、None、0、空字符串等），那么 Python 会继续计算右侧的表达式，并返回右侧表达式的值。
		
	例子：
	1. 当左侧是“真值”时：
	a = 10
	b = 5
	
	result = a or b  # 这里a是10，是真值
	步骤 1：计算 a，它的值是 10（真值）。
	步骤 2：由于 a 是真值，整个 or 表达式的结果是 10，Python 不会继续计算右侧的 b。
	
	2. 当左侧是“假值”时：
	a = 0
	b = 5
	
	result = a or b  # 这里a是0，假值
	步骤 1：计算 a，它的值是 0（假值）。
	步骤 2：由于 a 是假值，Python 继续计算右侧的表达式 b，并返回 b 的值，即 5。

![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228112551.png)
	3.print(3) or ""
	• 执行 print(3)
		○ print(3) 会输出 3，但它的 返回值是 None（print() 函数没有返回值）。
	• 计算 None or ""
		○ None 是 falsy，所以 or 继续执行 ""（空字符串）。
		○ "" 也是 falsy，但它作为 or 的最终结果返回。


**not**
• 在 Python 中，非零的数值（包括正数和负数）都是 True。
• 只有 0 被认为是 False。
• not 运算符会 对布尔值取反：
	 not True → False
     not False → True