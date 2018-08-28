import random
i = 0
while i < 3: 
    player = int(input("请输入 1.石头 2.剪刀 3.布"))
    cp = random.randint(1,3)
    if (player == 1 and cp == 2) or (player == 2 and cp == 3) or (player == 3 and cp ==1):
        print("玩家赢")
    elif player == cp:
        print("平局")
    else:
        print("电脑赢")
    i+=1

