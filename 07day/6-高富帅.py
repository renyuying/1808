height = int(input("请输入身高:"))
money = int(input("请输入身价:"))
face = int(input("请输入颜值分:"))
if (height > 180 and money > 1000000 and face > 99):
    print("高富帅")
elif (height >  1000000 and face > 99):
    print("富帅")
elif face > 99:
    print("帅")
elif (height < 160 and money < 100 and face < 60):
    print("矮穷挫")
