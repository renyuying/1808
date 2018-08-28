#coding=utf-8
list = [{'北京':{'面积':'1000平','人口':'200w'}'上海':{'面积':'600平','人口':'150w'}}]
for i in list:
    print(i)
    for k,v in i.tems():
            for j,l in v.items():
                print(k,j,l)
