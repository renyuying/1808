import random
cp = random.randint(1,10)
for i in range(1,10):
    player = int(input('请输入数字:'))
    if player < cp:
        print('猜小了')
    elif player > cp:
        print('猜大了')
    elif player == cp:
        print('猜对了')
        break
