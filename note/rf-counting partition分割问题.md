![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228153250.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228153302.png)
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228154151.png)

在整数分割问题中，count_partitions(n, m) 的含义是：

将整数 n 分割成若干部分，其中每个部分的大小不超过 m。
在分解过程中，我们将问题拆分为两种情况：
	1. 选择当前最大值 m：从 n 中减去 m，然后继续分割剩余部分。
	2. 不选择当前最大值 m：直接把最大值限制减少到 m - 1，继续分割整个 n。

count_partitions(n, m) = count_partitions(n - m, m) + count_partitions(n, m - 1)
	• count_partitions(n - m, m)：表示选择了 m 后分割剩下的部分。
	• count_partitions(n, m - 1)：表示不选择 m，只使用更小的数分割。

**为什么是 (2, 4) 和 (6, 3)？**
第一种情况：选择当前最大值
	• 选择一个 m = 4：
		- 如果我们至少使用一个 4，那么剩下的部分是 6 - 4 = 2。
		- 这意味着，我们要继续分割 2，并且分割的最大值仍然可以是 4（因为 4 可以继续被使用，只要 n 足够大）。
		- 因此，递归子问题为 count_partitions(2, 4)。
第二种情况：不选择当前最大值
	• 完全不使用 m = 4：
		- 如果不使用 4，那么我们只能使用小于 4 的值，即最大值限制变为 3。
		- 此时，我们需要分割完整的 6，但分割的每一部分大小不能超过 3。
		- 因此，递归子问题为 count_partitions(6, 3)。


**为什么不是 (3, 3)？**
如果你将第二种情况误解为 (3, 3)，那么你可能错误地认为：
	• 在第一种情况下，从 n = 6 减去 m = 4，得到剩余的 2。
	• 在第二种情况下，你可能以为要直接分割剩下的 6 - m = 3，并且最大值限制变为 3。
![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228154326.png)
