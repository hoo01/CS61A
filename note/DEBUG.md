[https://cs61a.org/articles/debugging/](https://cs61a.org/articles/debugging/)

# 一、回溯

# 二、doctest

- doctest 是 Python 标准库中的一个模块，它可以在 函数字符串（docstring） 里写测试代码，并在运行时自动验证这些测试。
- python -m doctest ex.py 会自动运行 ex.py 里的所有 doctest 测试。只在 docstring 里编写的测试会被 doctest 识别并运行。
- 运行 doctest 时 如果所有测试通过，不会有任何输出，但如果有错误，会显示对比的结果。

python -m doctest  file.py -v

可以看到详细的过程

## testmod

1.直接在.py文件里加  
 

from doctest import testmod
testmod()

直接显示测试结果

##   
run_docstring_examples

run_docstring_examples() 函数： run_docstring_examples() 函数是 doctest 模块提供的一种工具，它允许你指定一个特定的函数以及全局环境来验证该函数的 docstring 中的测试案例。

```
from doctest import run_docstring_examples
run_docstring_examples(divide_exact, globals(), True)
```

第一个参数：需要测试的函数，例如 divide_exact。

第二个参数：globals()，它是 Python 的内置函数，用于返回当前全局符号表。这个参数让 run_docstring_examples() 可以在全局作用域中找到该函数，并执行 docstring 中的代码。

第三个参数：True 表示以 详细模式 输出测试的结果。你可以选择设置为 False，只输出简单的通过或失败结果。

# 三、error types