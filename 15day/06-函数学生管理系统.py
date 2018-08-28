list = []
def add():
    d = {}
    name = input('请输入姓名:')
    age = int(input('请输入年龄:'))
    sex = input('请输入性别:')
    d['name'] = name
    d['age'] = age
    d['sex'] = sex
    list.append(d)
    print(list)
#add()
def find():
    name = input('请输入姓名:')
    for i in list:
        if i['name'] == name:
            print('姓名:%s\n年龄:%d\n性别:%s'%(i['name'],i['age'],i['sex']))
            break
def gai():
    name = input('请输入要修改的姓名:')
    for i in list:
        if i['name'] == name:
            print('1.修改姓名')
            print('2.修改年龄')
            print('3.修改性别')
            num = int(input('请输入选项:'))
            if num == 1:
                i['name'] = name
            elif num == 2:
                i['age'] = age
            elif num == 3:
                i['sex'] = sex
        print('修改成功')


def menu():
    print('欢迎来到学生管理系统')
    while True:
        print('1.添加学生')
        print('2.查找学生')
        print('3.修改学生')
        print('4.删除学生')
        print('5.退出系统')
        num = int(input('请选择功能:'))
        if num == 1:
            add()
        elif num == 2:
            find()
        elif num == 3:
            gai()
        elif num == 4:
            delete()
        elif num == 5:
            exit()
menu()
