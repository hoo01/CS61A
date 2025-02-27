如果你在 Python Console 里想切换到某个目录，不能用 cd，而应该用：

`import os`

`os.chdir("E:/CS61a/disc01")  # 替代 cd 命令`

`print(os.getcwd())  # 确保已经切换`

`import sys`

`sys.path.append("E:/CS61a/1")  # 让 Python 也能找到这个目录`

举例：

```python
import sys
import os

os.chdir("E:/CS61a/1")  # 切换目录
sys.path.append("E:/CS61a/1")  # 手动添加 Python 搜索路径

from race import race  # 现在可以成功导入
print(race(5, 7))
```