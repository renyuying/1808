'''
a = int(input("输入数字:"))
b = int(input("输入数字:"))
count = 0
num_sum = 0
if a >= b:
    count = b
    while count <= 2:
        num_sum += count
        count += 1
elif a < b:
    count = a
    while count <= b:
        num_sum += count
        count += 1
print(num_sum)
'''



a = int(input("输入数字:"))
b = int(input("输入数字:"))
num = 0
count = 0
if a >= b:
    count = a
    while count >= b:
        num+= count
        count -= 1
print(num)
