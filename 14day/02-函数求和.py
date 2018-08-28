def add(x,y):
    sum = 0
    for i in range(x,y+1):
        if x < y:
            sum += i
    print(sum)
a = int(input('请输入数字:'))
b = int(input('请输入数字:'))
add(a,b)  #发射指令


'''
#1-100的和
i = 0

for j in range(1,101):
    i+=j
print(i)
'''
