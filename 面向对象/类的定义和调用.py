# 1.怎么理解类?
# 类是一个变量和函数的集合
#
# 类就是把变量和函数包装在一起
#
# 2.怎么定义类
# class ClassName():
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# 可以看到，我们用class语句来定义一个类的，其实这就好比我们用def语句来定义一个函数一样。
#
# 竟然说类变量和方法的集合包，那么我们来创建一个类
class ClassA():
    var1 = 100
    var2 = 0.01
    var3 = '两点水'

    def fun1():
        print('我是fun1')

    def fun2():
        print('我是fun1')

    def fun3():
        print('我是fun1')

print(ClassA.var1)
print(ClassA.var2)
print(ClassA.var3)
ClassA.fun1()
ClassA.fun2()
ClassA.fun3()

# 3.怎么调用类属性和类方法
# 我们定义了类之后，我们怎么调用类里面的属性

# 类属性和方法的调用
# 类里面的变量叫属性 - 调用格式： 类.变量
# 类里面的函数叫方法 - 调用格式： 类.函数()



