![image.png](https://cdn.jsdelivr.net/gh/hoo01/image_auto/20250228163250.png)
练习见lab04 -divide
仔细品：
```python
def divide(numbers, range_list):
    # 返回的字典应该是：
# {
#    2: [10, 20, 30],
#    3: [15, 30],
#    5: [10, 15, 20, 25, 30]
# }
    return {x:[y for y in range_list if y % x == 0] for x in numbers if x > 2}
print(divide(2,3,5,10,15,20,25,30))
```

所以公式
`{<key exp>: <value exp> for <key_name> in <key_iter exp> if <key_filter exp>}`
`除了<value exp>外都是针对key的`