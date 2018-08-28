a = 123456
b = 'ryy'
account = input('请输入帐号:')
passwd = int(input('请输入密码:'))
i = 0
for i in range(1,4):
    if passwd == a and account == b:
        print('登录成功')
        option = int(input('请选择英雄范围 0,ADC 1,刺客 2法师:'))
        if option == 0:
            print('虞姬')
        elif option == 1:
            print('阿柯')
        elif option == 2:
            print('妲己')
    else:
        print("登录失败")
