# 1.什么是条件语句
# Python条件语句跟其他语言基本一致，都是通过一条或者多条语句执行结果（true后者false）来决定执行的代码块
# python程序语言指定任何非0和非空（null）值为true,0或者true为false
#
# 2.if语句的基本形式
# if 判断条件
#     执行语句....
# else
#     执行语句
#
#
#
# python语言有着严格的缩进要求，因此这里也需要注意缩进，也不要少了冒号：
# if 语句的判断条件可以用>（大于）、<(小于) 、==(等于)、 >=(大于等于)、 <=(小于等于) 来表示其关系

#例如：
#-*-coding:utf8-8-*-
results=59
if results>=60:
    print('及格')
else :
    print('不及格')

#上面也说到，非零数值、非空字符串、非空 list 等，判断为 True，否则为 False。因此也可以这样写：
num = 6
if num :
    print('Hello Python')

#如果num是空，那就打印不出来
num = ''
if num :
    print('Hello Python')

#很明显，空字符串是为 False 的，不符合条件语句，因此不会执行到 print('Hello Python') 这段代码。


#3.if语句多个判断条件的形式
# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……

# -*-coding:utf-8-*-
results = 89
if results > 90:
    print('优秀')
elif results > 80:
    print('良好')
elif results > 60:
    print('及格')
else :
    print('不及格')

#4.if语句多个条件同时判断
# 有时候我们会遇到多个条件的时候该怎么操作呢？
# 比如说要求 java 和 python 的考试成绩要大于 80 分的时候才算优秀，这时候该怎么做？
# 这时候我们可以结合 or 和 and 来使用。
# or （或）表示两个条件有一个成立时判断条件成功
#and （与）表示只有两个条件同时成立的情况下，判断条件才成功。

# -*-coding:utf-8-*-
java = 86
python = 68
if java > 80 and python > 80:
    print('优秀')
else :
    print('不优秀')
if (java >= 80 and java <90) or (python >= 80 and python <90):
    print('良好')
#注意：if 有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，此外 and 和 or 的优先级低于 >（大于）、<（小于）等判断符号，即大于和小于在没有括号的情况下会比与或要优先判断。
#先判断大于小于 在判断and or

#5.if嵌套
java = 86
python = 68
if java > 80:
    if python > 80:
        print('优秀')
    else:
        print('不优秀')
else:
    print('不优秀')

#不建议这样 因为嵌套的代码太多不容易阅读