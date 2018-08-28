for i in range(1,4):
    age = int(input("请输入年龄:"))
    money = float(input("请输入携带金钱:"))
    if age >= 18 and money >= 5:
        print("可以上网")
    else:
        print("坐在寝室")
    i+=1

