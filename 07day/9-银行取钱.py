account = 123456
passwd = 123456
money = 1000
a = int(input("请输入帐号:"))
b = int(input("请输入密码:"))
if a == account and b == passwd:
    print("登录成功")
else:
    print("非法账户")
c = float(input("请输入取钱金额:"))
if c > 1000:
    print("金额不足")
elif c < 1000:
    money = 1000-c
    print(money)


