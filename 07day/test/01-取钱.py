pwd = 123456
account = "123"
money = 9999
a = input("请输入帐号:")
b = int(input("请输入密码:"))
if a == account and b == pwd:
    print("登录成功")
    c = int(input("请输入取款金额:"))
    if c > money:
        print("余额不足")
    else:
        print("取款成功")
else:
    print("帐号或密码错误")

        

