#1.python的set和其他语言类似，是一个无序不重复的元素集，基本功能包括关系测试和消除重复元素
#set 和dict类似 但是set不存储value值的

#1.set的创建
#创建一个set，需提供一个list作为输入集合
set1=set([123,456,789])
print(set1)

#输出结果 显示出set是无序的 知不多dict保存的是key-value值，而set可以理解为保存key值
#重复元素会被过滤掉

set1=set([123,456,789,123,123])
print(set1)

# 2.set添加元素
# 通过add(key)方法添加元素到set中，可以重复添加，但不会有效果

set1=set([123,456,789])
print(set1)
set1.add(100)
print(set1)
set1.add(100)
print(set1)

#3.删除元素
#通过remove(key)方法删除set中的元素
set1=set([123,456,789])
print(set1)
set1.remove(456)
print(set1)


#4.set的运用
#因为set是一个无序不重复的元素集，因此，两个set可以做数学意义上的union(并集)，intersection(交集),difference(差集)等操作


set1=set('hello')
set2=set(['p','y','t','h','o','n'])
print(set1)
print(set2)

#交集(求两个set集合中相同的元素)）
set3=set1 & set2
print(set3)

#并集(合并两个set集合并去除重复的值)
set4=set1 | set2
print('\n并集 set4:')
print(set4)

#差集
set5=set1 - set2
set6=set2 - set1
print('\n差集 set5:')
print(set5)
print('\n差集 set6:')
print(set6)

list1 = [111,222,333,444,111,222,333,444,555,666]
set7=set1(list1)
print('\n去除列表元素的重复元素 set7')
print(set7)
