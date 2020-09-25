# 1.什么是元祖（tuple）
# 有序列表叫元祖:tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改。也就是元祖(tuple)是不变的，那么不可变是什么意思呢？
# 元祖(tuple)不可变是指当你创建了tuple时候，他就不能改变了，也就是说他也没有append()，insert()这样的方法
# 但他也有获取某个索引值的方法，但是不能赋值
#
# 为什么要有tuple
# 因为tuple不可变，所以代码更安全
# 所以建议用tuple代替list就尽量用tuple

# 2.怎么样创建元祖（tuple）
#
# 元祖创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

tuple1=('两点水','twowter','linagdainshui',123,456)
tuple2='两点水','twowter','liangdianshui',123,456

#创建空元素
tuple3=()

#元素中只包含以一个元素时，需要在元素后面添加逗号
tuple4=(123,)

#如果不加逗号，创建出来的就不是元祖（tuple）而是123这个数了。
# 这是因为括号（）既可以表示元祖tuple()，又可以表示数学公式中的小括号，
# 所以如果只有一个元素时，不加逗号，计算机根本没法认识你是要进行整数或者小数运算是表示元祖。
# 因此，python规定，这种情况下，按小数进行元算，计算结果自然是123，而如果你要表示元祖的时候，就需要加个逗号。
tuple5=(123)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)

#3.如何访问元祖（tuple）
#元祖下标索引也是从0开始，元祖（tuple）可以使用下标索引来访问元祖中的值。
#-*-coding:utf8-8-*-
tuple1=('两点水','twowter','linagdainshui',123,456)
tuple2='两点水','twowter','liangdianshui',123,456

print(tuple1[1])
print(tuple2[0])

# 4.修改元祖
# 元祖中的元素值是不允许修改的，但我们可以对元祖进行连接组合，还有通过修改其他列表的值从而影响tuple的值
#-*-coding:utf8-8-*-
list1=[123,456]
tuple1=('两点水','twowater','liangdianshui',list1)
print(tuple1)
list1[0]=789
list1[1]=100
print(tuple1)

#可以看到tuple1有4个元素，最后一个元素是一个list，list列表中有两个元素。
#我们影响list的值  从而来改变tuple的值



# 5.删除tuple
# tuple元祖中元素值是不允许删除的，但我们可以使用del语句删除整个元祖

#-*-coding:utf8-8-*-
list1=[123,456]
tuple1=('两点水','twowater','liangdianshui',list1)
del tuple1

#6.tuple(元祖)运算符
#与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

#7.元素内置函数
# 方法	描述
# len(tuple)	计算元组元素个数
# max(tuple)	返回元组中元素最大值
# min(tuple)	返回元组中元素最小值
# tuple(seq)	将列表转换为元组

#8.示例

name1 = ('一点水','两点水','三点水','四点水','五点水')
name2 = ('1点水','2点水','3点水','4点水','5点水')
list1 = [1,2,3,4,5]

#计算要元素个数
print(len(name1))

#连接两个元祖相加
print(name1 + name2)

#复制元祖
print(name1 * 2)

#元素是否存在（name1这个元祖中是否含有一点水这个元素）
print('一点水' in name1)

#元素的最大值
print(max(name2))

#元素的最小值
print(min(name2))

#将列表转换为元祖
print(tuple(list1))

