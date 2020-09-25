#比如int函数,将符合规则的字符串转化为整数
#str1 = '100'
#str2 = '300'
#print(str1 + str2)
#print(int(str1) + int(str2))

#文字类型的字符串不能强转为字符串
#如：
#print(int('88.88'))

#但这并不意味着浮点数不能转换为整数，而是小数形式的字符串强转为字符串
#print(int(88.88))

#这是因为int()函数是将数据转化为整数。如果是浮点数转化为整数，那么int()函数就会做取整处理
#只取整数的部分。

#print(float(8))
#print(complex(real [,imag]))

#coding=utf8

#复数
复数由实部和虚部两个部分构成
real+imag（虚部后缀为j或J）

aa=123-12j  #定义一个虚数
print(aa)    #输出这个虚数
print(aa.real)   #输出实部
print(aa.imag)    #输出虚部
print(aa.conjugate())    #输出该复数的共轭复数


int(x [,base ])	将x转换为一个整数
float(x )	将x转换到一个浮点数
complex(real [,imag ])	创建一个复数
str(x )	将对象 x 转换为字符串
repr(x )	将对象 x 转换为表达式字符串
eval(str )	用来计算在字符串中的有效 Python 表达式,并返回一个对象
tuple(s )	将序列 s 转换为一个元组
list(s )	将序列 s 转换为一个列表
chr(x )	将一个整数转换为一个字符
unichr(x )	将一个整数转换为 Unicode 字符
ord(x )	将一个字符转换为它的整数值
hex(x )	将一个整数转换为一个十六进制字符串
oct(x )	将一个整数转换为一个八进制字符串