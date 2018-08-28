def introduce(name,age):
    print('我的名字%s,年龄是%d'%(name,age))
introduce('小明',30)#位置参数
introduce('小明',age = 30)　#关键字参数
introduce(age = 30,name = '小张')
introduce(name = '老王',age = 78)


#关键字参数必须在位置参数后面
