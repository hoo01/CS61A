implement the function make_repeater that takes a one-argument function f and a positive integer n. It returns a one-argument function, where make_repeater(f, n)(x) returns the value of f(f(...f(x)...)) in which f is applied n times to x. For example, make_repeater(square, 3)(5) squares 5 three times and returns 390625, just like square(square(square(5))).
来自 <https://www.learncs.site/docs/curriculum-resource/cs61a/homework/hw02> 

`def make_repeater(f, n):`
    `"""Returns the function that computes the nth application of f.`
    `>>> add_three = make_repeater(increment, 3)`
    `>>> add_three(5)`
    `8`
    `>>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1`
    `243`
    `>>> make_repeater(square, 2)(5) # square(square(5))`
    `625`
    `>>> make_repeater(square, 3)(5) # square(square(square(5)))`
    `390625`
    `"""`
    `"*** YOUR CODE HERE ***"`

从上面的需求来看，我们需要设计一个函数 make_repeater(f, n)，它能够在返回的函数被调用时，正确地将 f 函数应用 n 次。要实现这个功能，闭包是非常合适的，因为它可以“记住”函数 f 和 n 的值，并且能够在返回的函数中使用这些值。


**how to use the inner function**
详见lab02

example:

`def multiply_by(m):`
    `def multiply(n):`
        `return n * m`
    `return multiply`

In this particular case, we defined the function multiply within the body of multiply_by and then returned it. Let's see it in action:

`multiply_by(3)`
`<function multiply_by.<locals>.multiply at ...>`
`>>> multiply(4)`
`Traceback (most recent call last):`
`File "<stdin>", line 1, in <module>`
`NameError: name 'multiply' is not defined`

A call to multiply_by returns a function, as expected. However, calling multiply errors, even though that's the name we gave the inner function. This is because the name multiply only exists within the frame where we evaluate the body of multiply_by.

So how do we actually use the inner function? Here are two ways:

`times_three = multiply_by(3) # Assign the result of the call expression to a name`
`times_three(5) # Call the inner function with its new name`
`15`
`multiply_by(3)(10) # Chain together two call expressions`
`30`

有一道很好的练习题目见lab02