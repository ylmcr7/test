# 1.什么是字典

#2.字典的创建
# 字典是一种可变容器模型，且可存储任意类型对象
# 字典的每个键值（key=>valus）对冒号（：）分割，每个对之间用逗号（，）分割，整个字典包括花括号（{}）中，
# 格式如下；
# dict = {key1 : value1,key2 : value2 }
#
# 注意：键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不变的
#2.创建dict（字典）实例
dict1={'liangdianshui':'11111','twowater':'22222','两点水':'33333'}
dict2={'abc':1234,1234:'abc'}

print(dict1)
print(dict2)

#3.访问dict(字典)

name = {'一点水':'131456780001','两点水':'1314567800002','三点水':'131456780003','四点水':'131456780004','五点水':'131456780005'}
print(name['两点水'])

#4.修改dict(字典)
#-*-coding:utf8-8-*-
dict1={'liangdianshui':'111111','twowater':'22222','两点水':'33333'}
print(dict1)
#新增一个键值对
dict1['jack']='444444'
print(dict1)
#修改键值对
dict1['liangdianshui']='555555'
print(dict1)


#5.删除dict(字典)
#通过del可以删除dict（字典）中的耨个元素，也能删除dict(字典)
#通过调用clear()方法可以清除字典中的所有元素

#-*-coding:utf8-8-*-
dict1={'liangdianshui':'11111','twowater':'222222','两点水':'33333'}
print(dict1)
#通过key值，删除对应的元素
del dict1['twowater']
print(dict1)
#删除字典中所有的元素
dict1.clear()
print(dict1)
#删除字典
del dict1

#6.dict(字典)使用注意的事项
#dict（字典）是不允许一个键创建两次的，但是在创建dict(字典)的时候如果出现一个键值赋予了两次，会以最后一次的赋予的值为准

#-*-coding:utf8-8-*-
dict1={'liangdianshui':'11111','twowater':'22222','两点水':'33333','twowater':'44444'}
print(dict1)
print(dict1['twowater'])

#dict(字典)键必须不可变，可是键可以用数字，字符串和元祖充当，但是就是不能使用列表
#-*-coding:utf8-8-*-
dict1={'liangdianshui':'11111',123:'22222',(123,'tom'):'33333','twowater':'44444'}
print(dict1)

# dict内部存放的顺序和key放入的顺序是没有任何关系
# 和list比较,dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而改变
# 需要占用大量的内存，内存浪费多

# list：
# 查找和插入的时间随着元素的增加而增加
# 占用空间少，浪费内存很少


#7.dict(字典)的函数和方法
# 方法和函数	描述
# len(dict)	计算字典元素个数
# str(dict)	输出字典可打印的字符串表示
# type(variable)	返回输入的变量类型，如果变量是字典就返回字典类型
# dict.clear()	删除字典内所有元素
# dict.copy()	返回一个字典的浅复制
# dict.values()	以列表返回字典中的所有值
# popitem()	随机返回并删除字典中的一对键和值
# dict.items()	以列表返回可遍历的(键, 值) 元组数组


print(len(dict1))
print(str(dict1))
print(type(dict1))
print(dict1.clear())
print(dict1.copy())
print(dict1.values())
# popitem()
# print(dict1)
print(dic.items(dict1))