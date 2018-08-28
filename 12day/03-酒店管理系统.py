import time
print('欢迎来到酒店'.center(30,'$'))
list = []
all_money = 0
while True:
    print('1.住店')
    print('2.离店')
    print('3.统计')
    print('4.退出')
    num = int(input('请输入选项:'))
    if num == 1:
        d = {}
        print('住店')
        name = input('请输入姓名:')
        card = int(input('请输入身份证号:'))
        d['name'] = name
        d['card'] = card
        d['time'] = int(time.time())
        d['rd'] = True
        list.append(d)
        print(list)
        print('入住成功')
    elif num == 2:
        print('离店')
        name = input('请输入姓名:')
        for i in list:
            if i['name'] == name:
                i['rd'] = False #离店
                endtime = int(time.time())
                swq = (endtime-i['time'])*10
                print('花了%.02f'%swq)
                money = float(input('请输入金额，不找零钱'))
                all_money += swq
                print('离店成功')
    elif num == 3:
        print('统计')
        account = int(input('请输入帐号:'))
        passwd = int(input('请输入密码:'))
        if account == 123 and passwd == 123:
            print('欢迎老板进入管理系统')
            num = int(input('请选择功能:'))
            count = 0
            if num == 1:
                print('今天住店%d'%len(list))
                for i in list:
                    if i['rd'] == False:
                        count+=1
                print('今天离店%d'%count)
                print('今天收益%.02f'%all_money)
    elif num == 4:
        print('退出')
        exit()
