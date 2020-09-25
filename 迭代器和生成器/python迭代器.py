# 迭代式python最强大的功能之一，是访问集合元素的一种方式。现在正式进入主题：迭代器，迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter()和 next(),且字符串，列表或元祖对象都可用于创建迭代器，迭代器对象可以使用常规
# for 语句进行遍历，也可以使用next()函数来遍历。

#实例：

#1.字符创创建迭代器对象
str1 = 'liangdianshui'
iter1 = iter (str1)

#2.list对象创建迭代器
list1 = [1,2,3,4]
iter2 = iter (list1)

#3.tuple（元祖）对象创建迭代器

tuple1 = (1,2,3,4)
iter3 = iter ( tuple1 )



#for 循环遍历迭代去对象
for x in iter1 :
    print( x , end = '' )
print('\n-------------------')

#next()函数遍历迭代器
while True :
    try :
        print( next ( iter3 ) )
    except StopIteration :
        break


