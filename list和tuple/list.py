#1.什么是list?
#list（列表）是python内置的一种数据类型
#是一个有序的集合，可以随时添加和删除其中的元素
#name = ['一点水','两点水','三点水','四点水','五点水']

#怎么创建list?
#name:列表名
#=：赋值符号
#[]:中括号
#, ：逗号

#列表就是用中括号[]括起来的数据，
#里面的每一个数据就叫元素。
#每个元素之间使用逗号分隔。
#列表的数据元素不一定是相同的数据类型

#list1=['两点水','towter','liangdianshui',123]
#rint(list1)


#3.如何访问list中的值？
#name = ['一点水','两点水','三点水','四点水','五点水']
#通过索引来访问列表
#print(name[2])
#索引是从0开始的

#通过方括号的形式来截取列表中的数据
#print(name[0:2])
#从0开始截取  但不包括2
#print('--------------------')
# print(name[0:2])
# print(name[:2])
# print(name[:])
# print(name[1:2])
# print(name[0:3])

#4.怎么更新list(列表)
# 还是一开始的例子，我们用代码记录了报名人的名字，那后面可能会有新人加入，也有可能会发现一开始写错名字了，想要修改。
# 这时候怎么办呢？
# 这时候可以通过索引对列表的数据项进行修改或更新，也可以使用 append() 方法来添加列表项。


#name = ['一点水','两点水','三点水','四点水','五点水']
#通过索引对列表的数据项进行修改或更新
# name[1]='2点水'
# print(name)

#使用append()方法来添加列表项
#name.append('六点水')
#print(name)


#5.怎么删除list里面的元素

#name = ['一点水','两点水','三点水','四点水','五点水']

#print(name)

#使用del语句删除列表中的元素
#del name[3]
#print(name)


#6.list运算符
#列表对 + 和 *的操作与字符串相似。_+ 号用于组合列表，* 号用于重复列表

# list1=[1,2,3,4]
# list2=[5,6,7,8]
#
# print(list2 + list1)     #组合
# print(len(list1))         #计算元素长度
# print(list2 * 4)         #复制
# print(1 in list1)         #元素是否存在于列表中
# for x in [1,2,3]:print(x)     #迭代


#7.list函数&方法

# 函数&方法	               描述
# len(list)              	列表元素个数
# max(list)	            返回列表元素最大值
# min(list)            	返回列表元素最小值
# list(seq)	            将元组转换为列表
# list.append(obj)	    在列表末尾添加新的对象
# list.count(obj)	        统计某个元素在列表中出现的次数
# list.extend(seq)     	在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)	        从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)	将对象插入列表
# list.pop(obj=list[-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)	    移除列表中的一个元素（参数是列表中元素），并且不返回任何值
# list.reverse()	        反向列表中元素
# list.sort([func])	    对原列表进行排序

#8.实例

#-*-coding:utf8-8-*-
#----------------------------------list的使用---------------------------
#1.一个产品，需要列出产品的用户，这个时候就可以使用一个list表示
user=['liangdianshui','weoater','两点水']
print('\n1.产品用户')
print(user)

#2.如果需要统计有多少个用户，这时候len()函数可以获得list里元素的个数
len(user)
print('\n2.统计有多少个用户')
print(len(user))

#3.此时，如果需要知道具体的用户呢？可以通过索引来访问list中的每一个位置的元素，索引是从0开始的
print('\n3.查看具体的用户')
print(user[0]+','+user[1]+','+user[2])

#4.突然来了一个新的用户，这时我们需要在原有饿list末尾加上一个用户
user.append('茵茵')
print('\n4.在末尾添加新用户')
print(user)

#5.又新增了一个用户，可是这个用户是VIP级别用户，需要房子啊第一位，可以通过insert方法插入到制定的位置
#注意：插入数据的时候注意是否越界，索引不能超过len(user)-1
user.insert(0,'VIP用户')
print('\n5.指定位置添加用户')
print(user)

#6.突然发现弄错了，"茵茵"就是"VIP用户"，因此，需要删除"茵茵"；pop()删除list末尾的元素
user.pop()
print('\n6.删除末尾用户')
print(user)

#7.过了一段时间，用户"liangdianshui"不玩这个产品了，删除了账号
#因此需要删除指定位置的元素，用pop(i)方法，其中i是索引位置
user.pop(1)
print('\n7.删除指定位置的list元素')
print(user)

#8.用户"两点水"想修改自己的昵称
user[2]='三点水'
print('\n8.把某个元素替换成别的元素')
print(user)

#9.单单保存用户昵称好像不够好，最好吧账号也放进去
#这里账号是整数类型，跟昵称的字符串类型不同，不过list里面的元素的数据类型是可以不同的
#而且list元素可以是另一个list
newUser=[['VIP用户',11111],['twowater',22222],['三点水',33333]]
print('\n9.不同元素类型的list数据')
print(newUser)