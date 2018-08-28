import random
def a():
    cp = random.randint(1,3)
    for i in range(1,4):
        player = int(input('请输入数字 1.石头 2.剪刀 3.布:'))
        if (player == 1 and cp == 2) or (player == 2 and cp == 3) or (player == 3 and player == 1):
            print('玩家赢')
        elif player == cp:
            print('平局')
        else:
            print('电脑赢')
a()
