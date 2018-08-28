print('欢迎来到学生管理系统'.center(30,'*'))
box = []
while True:
    print('1.录入')
    print('2.修改')
    print('3.查找')
    print('4.删除')
    print('5.退出')
    num = int(input('请选择功能:'))
    if num == 1:
        xjb = {}
        name = input('请输入姓名:')
        sex = input('请输入性别:')
        age = int(input('请输入年龄:'))
        xjb['name'] = name
        xjb['sex'] = sex
        xjb['age'] = age
        box.append(xjb)
        print(box)
    elif num == 2:
        name = input('请输入要修改的姓名:')
        for xjb in box:
            if xjb['name'] == name:
                print('1.修改姓名')
                print('2.修改性别')
                print('3.修改年龄')
                num = int(input('请选择修改功能'))
                if num == 1:
                    name = input('请重新输入姓名:')
                    name = name.strip()
                    xjb['name'] = name
                elif num == 2:
                    sex = input('请重新输入性别:')
                    xjb['sex'] = sex
                elif num == 3:
                    while True:
                    age = int(input('请重新输入年龄:'))
                    if age < 1 or age > 120:
                        print('重新输入')
                        continue
                    else:
                        break
                    xjb['age'] = age
                print('修改成功')
                break
    elif num == 3:
        name = input('请输入查找的姓名:')
        flag = False
        for xjb in box:
            if xjb['name'] == name:
                print('姓名\t性别\t年龄')
                print('%s\t%s\t%s\t'%(xjb['name'],xjb['sex'],xjb['age']))
                flag = True:
                break
            if flag:
                print('查到了')
            else:
                print('查无此人')
    elif num == 4:
        name = input('请输入要删除的姓名:')
        for xjb in box:
            if xjb['name'] == name:
                num = int(input('您确定要删除　1:Yes  2:No'))
                if num == 1:
                    box.remove(xjb)
                print('删除成功')
                break
    elif num == 5:
        print('退出')
        exit()
