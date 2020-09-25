# 可以通过return[表达式]语句用于退出函数，选择性地调用方返回一个表达式
#
# 不带参数值的return语句返回none
#
# 具体示例：

# -*- coding: UTF-8 -*-
# def sum(num1,num2):
#     #两数之和
#     if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
#         raise TypeError('参数类型错误')
#     return num1+num2
#
# print(sum(1,2))

# 这个示例，还通过内置函数isinstance()进行数据类型检查，
# 检查调用函数时参数是否是整形和浮点型。如果参数类型不对，会报错，提示 参数类型错误,

#函数返回多个值。
def division ( num1, num2 ):
    #求商与余数
    a = num1 % num2
    b = (num1-a) / num2
    return b , a

num1 , num2 = division(9,4)
tuple1 = division(9,4)

print(num1,num2)
print(tuple1)

tuple2 = (1,2,3,4)
print(tuple2[0])

认真观察就可以发现，尽管从第一个输出值来看，返回了多个值，实际上是先创建了一个元组然后返回的。

回忆一下，元组是可以直接用逗号来创建的，观察例子中的 ruturn ，可以发现实际上我们使用的是逗号来生成一个元组。

Python 语言中的函数返回值可以是多个，而其他语言都不行，这是Python 相比其他语言的简便和灵活之处。

Python 一次接受多个返回值的数据类型就是元组。