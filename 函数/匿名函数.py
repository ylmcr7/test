# 有没有想过定义一个很短的回调函数，但又不想用def的形式去写那么长的函数，那么有没有快捷方式呢？
# 答案是有的。
#
# python使用lambda来创建匿名函数，也就是不再使用def语句这样的标准的形式去定义一个函数。
#
# 匿名函数主要有以下特点：
# lambda 只是一个表达式，函数体比def简单很多
# lambda 的主体是一个表达式，。而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去
# lambda 函数有自己的命名空间，且不能访问自由参数列表之外或全局命名空间里的参数

# 基本语法
# lambda [arg1 [,arg2,.....argn]]:expression

#示例

#-*- coding: UTF-8 -*-
sum = lambda num1 ,num2 : num1 + num2;
print(sum( 1 , 2 ))

# 注意： 尽管lambda表达式允许你定义简单函数，但是它使用是有限制的。你只能指定单个表达式，它的值就是最后的返回值。
# 也就是说不能包含其他的语言特性了，包括多个语句、条件表达式、迭代以及异常处理等。
#
# 匿名函数中，又一个特别需要注意的问题，比如。把上面的列子改一改

# -*- coding: UTF-8 -*-
num2 = 100
sum1 = lambda num1 : num1 + num2 ;

num2 = 10000
sum2 = lambda num1 : num1 + num2 ;

print( sum1( 1 ) )
print( sum2( 1 ) )

输出的结果是是10001  10001 而不是 101,10001

这主要在于lambda表达式中num2是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。
所以建议还是遇到这种情况还是使用第一种解法。