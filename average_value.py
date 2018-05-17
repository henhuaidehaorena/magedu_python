#要求：輸入n個數，計算每次輸入后的平均值
# -*- coding: UTF-8 -*-
#coding=utf-8 #等同於上面的聲明方式
#避免中文編碼異常

n=0
sum=0
while 1:
    digit=int(input('please input a digit:'))
    n=n+1
    sum=sum+digit
    average=sum/n
    print('average value=',average)
