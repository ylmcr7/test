# -*- coding: UTF-8 -*-

# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i, j, i*j),end='')
    print()

#判断闰年
year = int(input("请输入年份"))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0} 是闰年' .format(year))
else:
    print('{0} 不是闰年' .format(year))


