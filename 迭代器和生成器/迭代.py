# 1.什么叫做迭代？
# 比如我门在java中，我们通过list集合的下标来遍历list集合中的元素，在python中，给定一个list或tuple，我们
# 可以通过for循环来遍历这个list或tuple，这种变量就是迭代。
#
# 可是pyhton 的for 循环抽象成都要高于java的for 循环，为什么这样说呢？因为python的for 循环不仅仅可以用在list
# 或tuple上，还可以作用在其他迭代对象上。
#
# 也就是说,只要是迭代的对象，无论有没有下标，都是可以迭代的。

# -*- coding: UTF-8 -*-
#1.for 循环迭代字符串
for char in 'liangdianhshui' :
    print( char , end = '' )
print('\n')

#2.for循环迭代list
list1 = [1,2,3,4,5]
for num1 in list1:
    print( num1 , end = '' )
print('\n')

#3.for 循环也可以迭代dict （字典）
dict1 = {'name':'两点水','arg':'23','sex':'男'}
for key in dict1:
    print( key , end = '' )
print('\n')

for value in dict1.values() :
    print( value , end = '' )
print('\n')

#如果list里面一个元素有两个变量，也是很容易迭代的
for x , y in [ (1,'a'),(2,'b'),(3,'c')] :
    print( x ,y )
