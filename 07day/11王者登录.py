account = 123
passwd = "zxc"
a = int(input("请输入帐号:"))
b = input("请输入密码:")
if a == account and b == passwd:
    print("登录成功")
    hero = int(input("请选择职业\n1.法师\n2.刺客\n3.ADC\n4.辅助"))
    if hero == 1:
        print("诸葛亮,妲己")
    elif hero == 2:
        print("阿柯,韩信")
    elif hero == 3:
        print("百利守约,虞姬")
    elif hero == 4:
        print("明世隐,大乔")
else:
    print("非法账户")
