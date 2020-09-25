#1.类方法如何调用类属性

# class ClassA():
#     var1 = '两点水'
#
#     @classmethod
#     def fun1(cls):
#         print('我是 fun1' + cls.var1)
#
# ClassA.fun1()


#类方法上面多了一个@calssmethod，这是干嘛用的呢？
# 这是用于声明下面的函数是类函数。从名字就很好理解了
#
# class就是类，method就是方法
# 一定，没使用的话 会报错
#
#
# 如果没声明类的方法，方法参数中就没有cls,就没办法通过cls获取到类属性
#
# 因此类方法，想要调用类属性，需要以下步骤
#
# 在方法上面，用@classmethod声明该方法是类方法，只有声明了是类方法，才能使用类属性
# 类方法想要使用类属性，在第一个参数中，需要写上cls，cls是class的缩写，其实意思就是把这个类
# 作为参数，传给自己，这样就可以使用类属性了。
# 类属性的使用方式就是cls.变量名
#
# 无论是@classmethod还是cls，都是不能省去的。



#2.类方法传参


class ClassA():
    var1 = '两点水'

    @classmethod
    def fun1(cls, age):
        print('我是 fun1' + cls.var1)
        print('年龄: ' + str(age))

ClassA.fun1(18)

