# 1.什么是循环语句
# 一般编程语言都有循环语句，为什么呢？
#
# 那就问一下自己，我们弄程序是为了干什么？
#
# 那肯定是为了方便我们工作，优化我们的工作效率啊。
#
# 而计算机和人类不同，计算机不怕苦也不怕累，也不需要休息，可以一直做。
#
# 你要知道，计算机最擅长就是做重复的事情。
#
# 所以这时候需要用到循环语句，循环语句允许我们执行一个语句或语句组多次。
#
# 循环语句的一般形式如下：

# 在 Python 提供了 for 循环和 while 循环。
#
# 这里又有一个问题了，如果我想让他运行了一百次之后停止，那该怎么做呢？
#
# 这时候需要用到一些控制循环的语句：
# 循环控制语句	描述
# break	在语句块执行过程中终止循环，并且跳出整个循环
# continue	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
# pass	pass 是空语句，是为了保持程序结构的完整性

#2.for循环

#基本的语法格式：
# for iterating_var in sequence:
#     statements(s)

#列子

for letter in 'Hello 两点水':
    print(letter)

dict1 = {'1点水':'小学生','两点水':'初中生','三点水':'高中生'}
for i in dict1:
    print(i)

list = (1,2,3,4,5,6)
for i in list:
    print(i)

tuple = (7,8,9,10)
for i in tuple:
    print(i)


#整数和浮点数是不能直接放在for循环里面的
# a = 100
# b = 0.01
# for i in a:
#     print(i)
# for i in b:
#     print(i)

#3.range()函数
# for循环还常常和range（）函数搭配使用的。
#看看range
for i in range(3):
    print(i)


for i in range(6,9):
    print(i)
#使用 range(x) 函数，就可以生成一个从 0 到 x-1 的整数序列。

#我们发现 每次都是递增1  我们想让他递增2呢
for i in range (0,10,2):
    print(i)
# 所以 range 函数还有一个三个参数的。
#
# 比如 range(0,10,2) , 它的意思是：从 0 数到 10（不取 10 ），每次间隔为 2 。

#4.while循环语句
count = 1
sum1 = 0
while count <= 100:
    sum1 = sum1 + count
    count = count + 1
print(sum1)
#这个例子是计算1到100的和

#5.for循环和while循环
# 之前也提到过了，如果一种语法能表示一个功能，那没必要弄两种语法来表示。
#
# 竟然都是循环，for 循环和 while 循环肯定有他们的区别的。
#
# 那什么时候才使用 for 循环和 while 循环呢？
#
# for 循环主要用在迭代可迭代对象的情况。
#
# while 循环主要用在需要满足一定条件为真，反复执行的情况。 （死循环+break 退出等情况。）
#
# 部分情况下，for 循环和 while 循环可以互换使用。
#
#例如：
print('---------------------------------------------')
# for i in range(0,10):
#     print(i)
#
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

#虽然打印的结果是一样的，但是细细品味你会发现，他们执行的顺序和知道的条件是不同的。

#6.嵌套循环

#for 循环嵌套语法

# for iterating_var in sequence:
#     for iterating_var in sequence:
#         statements(s)
#     statements(s)
#
# while循环嵌套语法
# while expression:
#     while expression:
#         statements(s)
#     statements(s)
#除此之外，你也可以在循环体内嵌入其他的循环体，如在 while 循环中可以嵌入 for 循环， 反之，你可以在 for 循环中嵌入 while 循环
#例子：
#当我们需要判断 sum 大于 1000 的时候，不在相加时，可以用到 break ，退出整个循环。

# count = 1
# sum  = 0
# while (count <= 100):
#     sum = sum + count
#     if ( sum > 1000):
#         break
#     count = count + 1
# print(sum)


# count = 1
# sum = 0
# while (count <= 100):
#     if (count % 2 == 0):
#         count = count + 1
#         continue
#     sum = sum + count
#     count = count + 1
# print(sum)

for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print('%d是一个合数' % num)
            break
    else:
        print('%d是一个质数' % num)
