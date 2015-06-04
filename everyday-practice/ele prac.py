#coding:utf-8
for i in range(1, 201):
    pri = int(i**2)
    if pri <= 10:
       print(i)
    if pri/10 > 0 and pri<=100 and pri%10 ==pri/10:
       print(i)
    if pri/100 > 0 and pri<=1000 and pri%10 == pri/100:
        print(i)
    if pri/1000 > 0 and pri<=10000 and str(i**2)[0] ==str(i**2)[-1] and str(i**2)[1] ==str(i**2)[-2] :
        print(i)
    if pri/10000 > 0 and pri<=100000 and str(i**2)[0] ==str(i**2)[-1] and str(i**2)[1] ==str(i**2)[-2]:
        print(i)

# _*_ coding=utf-8 _*_
for n in range(1, 200):
    sq = n * n
    str_sq = str(sq)
    istr_sq = str_sq[::-1]  #list中括号中冒号分割的第三个值表示步长#步长-1表示倒着每个值都取出来
    if str_sq == istr_sq:
        print n






