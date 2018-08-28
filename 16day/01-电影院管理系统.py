move = []
def add():
    d = {}
    name = input('请输入片名:')
    sort = input('请输入影片类型:')
    time = input('上映时间:')
    d['name'] = name.strip()
    d['sort'] = sort
    d['time'] = time
    move.append(d)
    print(move)
    print('添加成功')

def delete():
    name = input('请输入要删除的片名:')
    for d in move:
        if d['name'] == name:
            move.remove(d)
            print('删除成功')
            break

def xiu():
    name = input('请输入要修改的片名:')
    name = name.strip()
    for d in move:
        if d['name'] == name:
            print('1.修改片名')
            print('2.修改影片类型')
            print('3.修改上映时间')
            num = int(input('请选择功能:'))
            if num == 1:
                name = input('请输入新的片名:')
                d['name'] = name
            elif num == 2:
                sort('请输入新的影片类型:')
                d['sort'] = sort
            elif num == 3:
                tiem = input('请输入新的上映时间:')
                d['time'] = time
            print('修改成功')
            #print(move)
            break

def cha():
    name = input('请输入要查找的片名:')
    name = name.strip()
    flag = False
    for d in move:
        if d['name'] == name:
            flag = True
            print('片名\t类型\t上映时间')
            print('%s\t%s\t%s'%(d['name'],d['sort'],d['time']))
            break
    if not flag:
        print('搜索无效')

def menu():
    while True:
        print('欢迎管理员来到电影管理系统'.center(30,'*'))
        print('1.增加电影')
        print('2.删除电影')
        print('3.修改电影')
        print('4.查找电影')
        print('5.退出系统')
        num = int(input('请选择功能:'))
        if num == 1:
            add()
        elif num == 2:
            delete()
        elif num == 3:
            xiu()
        elif num == 4:
            cha()
        elif num == 5:
            exit()
menu()
