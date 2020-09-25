#因为迭代器和生成器是互通的，因此有些知识点需要综合在一起
#1.反向迭代
#反向迭代，应该也是常有的需求了，比如从一开始迭代的例子里，有个输出list的元素，从1到5的

list1 = [1,2,3,4,5]
for num1 in list1 :
    print( num1 , end = '' )
print('\n')
#那么从5到1呢？ 也很简单，python中有内置的函数reserved()

list1 = [1,2,3,4,5]
for num1 in reversed(list1) :
    print( num1 , end = '' )

# 反向迭代很简单，可是要注意一点：反向迭代仅仅当对象的大小可以预先确定或者对象实现了_reversed_()的特殊方法
# 时才能生效。如果两者都不符合，那必须先将对象转换为一个列表才行
#
# 其实很多时候我们可以通过在自定义类上实现 __reversed__() 方法来实现反向迭代。不过有些知识点在之前的篇节中还没有提到，不过可以相应的看下，有编程基础的，学完上面的知识点应该也能理解的。





# -*- coding: UTF-8 -*-

# class Countdown:
#     def __init__(self, start):
#         self.start = start
#
#     def __iter__(self):
#     	# Forward iterator
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#
#     def __reversed__(self):
#     	# Reverse iterator
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1
#
# for rr in reversed(Countdown(30)):
#     print(rr)
# for rr in Countdown(30):
#     print(rr)
print('\n')
#2.同时迭代多个序列

#同时迭代多个序列，每次分别从一个序列中取一个元素，你遇到过这样的需求吗？
names = ['liangdianshui' , 'twowater' , '两点水']
ages = [18,19,20]
for name, age in zip(names, ages):
    print(name,age)


#这是分隔符
print('\n')

# 其实 zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b。 一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。注意理解这句话喔，也就是说如果 a ， b 的长度不一致的话，以最短的为标准，遍历完后就结束。
#
# 利用 zip() 函数，我们还可把一个 key 列表和一个 value 列表生成一个 dict （字典）,如下

# -*- coding: UTF-8 -*-
names = ['liangdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
dict1= dict(zip(names,ages))
print(dict1)

#这里提一下， zip() 是可以接受多于两个的序列的参数，不仅仅是两个。

