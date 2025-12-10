# Eval()函数
# eval(expression[, globals[, locals]])
# expression ： 表达式。
# globals ： （可选参数)变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals ： (可选参数)变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
import math

a = 10
print(eval('a+1'))
print(eval('math.sqrt(5)'))
g = {'a': 2}
print(eval('a+1', g))  # 3
l = {'b': 3}
print(eval('a+b', g, l))  # 5

