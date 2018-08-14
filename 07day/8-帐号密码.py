account = 123456
passwd = "abc"
a = int(input("请输入帐号:"))
b = input("请输入密码:")
if a == account and b == passwd:
    print("登录成功")
elif (a != account and b == passwd):
    print("帐号错误")
elif (a == account and b != passwd):
    print("密码错误")
