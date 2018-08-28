import random
i = 0
while i < 9: 
    cp = random.randint(1,50)
    player = int(input("请输入数字:"))
    if player == cp:
        print("猜对了")
    else:
        print("猜错了")
    i+=1
