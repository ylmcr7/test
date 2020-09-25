#1.函数的参数类型
#设置与传递参数是函数的重点，而python的函数对参数的支持非常灵活
#主要的类型参数有：默认参数、关键字参数（位置参数）、不定长参数。

#2.默认参数
# 有时候，我们自定义的函数中，如果调用的时候没有设置参数，需要给个默认值，这时候就需要用到默认值参数了。
# 默认参数，只要在构造函数参数的时候，。给参数复制就可以了

# -*-coding:utf-8 -*-
# def print_user_info( name , age , sex = '男'):
#     #打印用户信息
#     print('昵称: {}'.format(name) ,end='')
#     print('年龄: {}'.format(age) , end='')
#     print('性别: {}'.format(sex))
#     return;
#
# print_user_info('两点水' , 18 , '女')
# print_user_info('三点水' , 25)

# 从输出结果可以看到，当你设置了默认参数的时候，在调用函数的时候，不传该参数，就会使用默认值。
#
# 但是这里需要注意的一点是：只有在形参表末尾的那些参数可以有默认参数值，也就是说你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。
#
# 这是因为赋给形参的值是根据位置而赋值的。例如，def func(a, b=1) 是有效的，但是 def func(a=1, b) 是 无效 的。
#
# 默认值参数就这样结束了吗？
#
# 还没有的，细想一下，如果参数中是一个可修改的容器比如一个 lsit （列表）或者 dict （字典），那么我们使用什么来作为默认值呢？
#
# 我们可以使用 None 作为默认值。就像下面这个例子一样：

#如果b是一个list,可以是None作为默认值
def print_info( a , b=None):
    if b is None :
        b =[]
    return;

def print_info( a , b = []):
    return;

# 对不对呢？
#
# 运行一下也没发现错误啊，可以这样写吗？
#
# 这里需要特别注意的一点：默认参数的值是不可变的对象，比如None、True、False、数字或字符串，如果你像上面的那样操作，当默认值在其他地方被修改后你将会遇到各种麻烦。
#
# 这些修改会影响到下次调用这个函数时的默认值。
#
# 示例如下：

# def print_info( a , b = []):
#     print(b)
#     return b ;
# result = print_info(1)
# result.append('error')
# print_info(2)

# 认真观察，你会发现第二次输出的值根本不是你想要的，因此切忌不能这样操作。
#
# 还有一点，有时候我就是不想要默认值啊，只是想单单判断默认参数有没有值传递进来，那该怎么办？
#
# 我们可以这样做：

_no_value = object()
def print_info( a , b = _no_value ):
    if b is _no_value :
        print('b没有赋值')
    return;

# 3.关键字参数（位置参数）
# 一般情况下，我们需要给函数传参的时候，是要桉顺序来的，如果不对应顺序，就会传错值。
# 不过在python中，可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序，
# 还被称之为关键字参数。
#
# 使用关键字参数有两个优势：
#
# 由于我们不必担心参数的顺序，使用函数变得更加简单了。
# 假设其他参数都有默认值，我们可以只给我们想要的那些参数复制
#
# 具体看例子：

# -*- coding:utf-8: -*-
def print_user_info( name , age , sex = '男'):
    #打印用户信息
    print('昵称: {}'.format(name) , end='')
    print('年龄: {}'.format(age) , end='')
    print('性别: {}'.format(sex))
    return;
print_user_info( name = '两点水' , age = 18 ,sex = '女')
print_user_info( name = '两点水' , sex = '女' , age = 18)

#4.不定长参数
# 或许有些时候，我们在设计函数的时候，我们有时候无法确定传入的参数个数。
# 那么我们就可以使用不定长参数。
# python提供了一种元祖的方式来接受没有直接定义的参数。这种方式在参数前面追加 *
# 如果在函数调用时没有指定参数，它就是一个空元祖。我们可以不向函数传递未命名的变量。

def print_user_info( name , age , sex = '男' , * hobby):
    #打印用户信息
    print('昵称: {}'.format(name) , end='')
    print('年龄: {}'.format(age) , end='')
    print('性别: {}'.format(sex) , end='')
    print('爱好: {}'.format(hobby))
    return;
print_user_info( '两点水' , 18 ,'女' , '打篮球' , '打羽毛球' , '跑步')
#
# 通过输出的结果可以知道，*hobby是可变参数，且 hobby 其实就是一个 tuple （元祖）
#
# 可变长参数也支持关键字参数（位置参数），没有被定义的关键参数会被放到一个字典里。
#
# 这种方式即是在参数前边加 **,更改上面的示例如下：

# -*- coding: UTF-8 -*-

def print_user_info( name ,  age  , sex = '男' , ** hobby ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;
print_user_info( name = '两点水' , age = 18 , sex = '女', hobby = ('打篮球','打羽毛球','跑步'))
#通过对比上面的例子和这个例子，可以知道，*hobby是可变参数，且 hobby其实就是一个 tuple （元祖），**hobby是关键字参数，且 hobby 就是一个 dict （字典）


#5.只接受关键字参数
#关键字参数使用起来简单，不容易参数出错，那么有些时候，我们定义的函数希望某些参数强制使用关键字参数传递，
# 这时候该怎么办呢？
#将强制关键字参数放到某个 * 参数或者单个 * 后面就能达到这种效果，

#-*- coding: utf-8: -*-
def print_user_info( name , *, age , sex = '男'):
    #打印用户信息
    print('昵称: {}'.format(name) , end='')
    print('年龄: {}'.format(age) ,end='')
    print('性别: {}'.format(sex))
    return;

#调用 print_user_info函数
print_user_info( name = '两点水' , age = 18 ,sex = '女')

#这种写法会报错，因为 age, sex 这两种参数强制使用关键字参数
print_user_info( '两点水' , 18 ,'女')
print_user_info('两点水',age='22',sex='男')

通过例子可以看，如果 age , sex 不使用关键字参数是会报错的。

很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具有可读性。使用强制关键字参数也会比使用 **kw 参数更好且强制关键字参数在一些更高级场合同样也很有用。



