print('欢迎来到麒麟网咖'.center(30,"$"))
list = []
while True:
    print('1.上机')
    print('2.下机')
    print('3.退出系统')
    num = int(input('请选择功能:'))
    if num == 1:
        d = {}
        card = int(input('请输入身份证号:'))
        money = float(input('请输入金额:'))
        d['card'] = card
        d['money'] = money
        d['time'] = int(tme.time())
        list.append(d)
        print(list)
    elif num == 2:
        print('下机')
        card = int(input('请输入身份证号:'))
        for i in list:
            if i['card'] == card:
                endtime = int(time.time())
                diff_money = (endtime-i['time'])*10
                diff = i['money']-diff_money
                if diff < 0:
                    print('您欠了%.02f元'%diff)
                    money = float(input("请输入金额:"))
                    if money >= diff:
                        print('找零%d'%(money-diff))
                    else:
                        print('输入的钱不足,欠了%.02f元'%diff)
                    print('')
            else:

    elif num == 3:
        print('退出')
        exit()
