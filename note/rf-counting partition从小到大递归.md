`count_partitions(n, smallest) =` 
`count_partitions(n - smallest, smallest) + count_partitions(n, smallest + 1)`

• 第一项 count_partitions(n - smallest, smallest):
选择 smallest，继续使用它，减少 n。
• 第二项 count_partitions(n, smallest + 1):
不使用 smallest，改用更大的数。

递归终止条件
	• n == 0：找到了一种有效组合，返回 1
	• n < 0：无法组成 n，返回 0
	• smallest > n：没有更多数可以尝试，返回 0

