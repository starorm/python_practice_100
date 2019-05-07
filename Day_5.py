#!/usr/bin/env python
#!-*-codinng:utf-8 -*-
#!@Time   :2019/5/7 22:28
#!@Author :star xu
#!@File   :Day_5.py

#题目 输入三个整数x,y,z，请把这三个数由小到大输出。

#程序分析 练练手就随便找个排序算法实现一下，偷懒就直接调函数。

x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(x, y, z)

import re
lst = map(int, re.split(r"[ |,]+",input("Enter Three Number: ")))

for item in sorted(lst):
    print (item)


#---------------------
#作者：杰瑞26
#来源：CSDN
#原文：https://blog.csdn.net/Jerry_1126/article/details/85083261
#版权声明：本文为博主原创文章，转载请附上博文链接！