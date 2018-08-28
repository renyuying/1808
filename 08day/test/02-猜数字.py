import random
i = 0
while i < 10:
    cp = random.randint(1,10)
    player = int(input("请输入数字"))
    if player < cp:
        print("猜小了")
    elif player == cp:
        print("猜对了")
    else:
        print("猜大了")
    print("随机的数字是%d"%i)
    i+=1
