import random
for i in range(1,11):
    cp = random.randint(1,10)
    for n in range(1,101):
        player = int(input('请输入数字:'))
        if player < cp:
            print('猜小了')
#        elif player == cp:
 #           print('猜对了') 
            #break
        else:
            print('猜大了')
            if player == cp:
                print('猜对了')
                break


