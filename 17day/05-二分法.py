list = [1,34,67,23,44,89,100,245]
'''
for p,i in enumerate(list):
    print(p,i)
    if i == 44:
        print(p)
        break
'''
max = len(list)-1
num == 44
count = 0
while True:
    center = int((min+max)/2)
    if list[center] > num:
        max = center-1
    elif list[center] < num:
        min = center +1
    elif list[center] == num:
        print(center)
        break
    count+=1
print(count)
