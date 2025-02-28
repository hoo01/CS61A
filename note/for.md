![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228160759.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228160810.png)
sequence unpack
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228160824.png)
这里使用的是 序列解包（Sequence Unpacking）for x, y in pairs: 语句中的 x, y 并不是接收整个子列表 [1, 2]、[2, 2] 等，而是把子列表中的每个元素逐个拆开并赋给 x 和 y。
例如：
	• 对于子列表 [1, 2]，x 被赋值为 1，y 被赋值为 2。
	• 对于子列表 [2, 2]，x 被赋值为 2，y 被赋值为 2。
	• 对于子列表 [3, 2]，x 被赋值为 3，y 被赋值为 2。
	• 对于子列表 [4, 4]，x 被赋值为 4，y 被赋值为 4。
	
你再品
```python
pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0

for pair1, pair2 in zip(pairs, pairs[1:]):
    x = pair1
    y = pair2
    if x == y:
        same_count = same_count + 1

print(same_count)