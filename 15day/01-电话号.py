def phone():
    while True:
        a = str(input('请输入手机号:'))
        if a.startswith('1') and len(a) == 11:
            print('输入成功')
        else:
            print('输入不合法')
phone()
