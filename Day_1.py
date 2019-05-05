#!/usr/bin/env python
#!-*-codinng:utf-8 -*-
#!@Time   :2019/5/5 21:19
#!@Author :star xu
#!@File   :Day_1.py

#题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
total = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j)and(j!=k)and(i!=k):
                total += 1
                print(i,j,k)
print(total)

#简便方法 用itertools中的permutations即可。
import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1
print(sum2)
