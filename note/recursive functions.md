所以递归函数就是一个函数，其主体要么直接调用自身，要么间接调用自身
So a recursive function is a function whose body calls itself either directly or indirectly.

一个简单的递归案例：
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152413.png)
- The def statement header is similar to other functions
- Conditional statements check for base cases
- Base cases are evaluated without recursive calls
- Recursive cases are evaluated with recursive calls

**Mutual recursion**
相互递归是指两个不同的函数互相调用
Mutual recursion occurs when two different functions call each other.
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152546.png)
![](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152546.png)