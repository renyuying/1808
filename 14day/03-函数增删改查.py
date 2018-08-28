list = []
while True:
    print('1.增加')
    print('2.删除')
    print('3.修改')
    print('4.查找')
    print('5.退出')
    num = int(input('请选择功能:'))
    if num == 1:
        print('增加')
        d = {}
        name = input('请输入姓名:')
        age = int(input('请输入年龄:'))
        d['name'] = name
        d['age'] = age
        list.append(d)
        print(list)
    elif num == 2:
        print('删除')
        name = input('请输入要删除的姓名:')
        if d['name'] == name:
            list.remove(d)
            print('删除成功')
    elif num == 3:
        print('修改')
        name = input('请输入要修改的姓名:')
        for d in list:
            if d['name'] == name:
                print('1.修改姓名')
                print('2.修改年龄')
                num = int(input('请输入选项:'))
                if num == 1:
                    name = input('请输入新的名字:')
                    d['name'] == name
                elif num == 2:
                    age = int(input('请输入新的年龄:'))
                    d['age'] == age
                list.append(d)
                print(list)
                break
    elif num == 4:
        print('查找')
        flag = False
        name = input('请输入要查找的姓名:')
        for d in list:
            if d['name'] == name:
                print('姓名\t年龄')
                print('%s\t%d'%(d['name'],d['age']))
                flag == True
                break
        if flag == False:
            print('查无此人')
    elif num == 5:
        print('已退出')
        exit()
