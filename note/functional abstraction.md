函数抽象就是给某个计算过程起个名字，然后整个过程都用这个名字来引用，而不用担心具体的实现细节。
So functional abstraction is giving a name to some computational process and thenreferring to that process as a whole without worrying about its implementation details.
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228151933.png)
Choosing Names
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228151952.png)

**Which values deserve a name何时需要取名**
1.例如“我计算了a平方加b平方的平方根，既在条件语句中又在赋值语句中，最好给这个东西取个名字，然后在这里和那里都用一下。”
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152025.png)
2.避免表达式过于复杂，最好将有意义的部分提取出分，比如这个二次方程的判别式，这样更易阅读，而不是试图理解整个嵌套
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152055.png)
3.但有时取长的名字更好
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152106.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228152115.png)
