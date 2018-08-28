import random
a = list
def addnum():
    list = []
    while True:
        num = random.randint(1,101)
        if num not in list:
            list.append(num)
        if len(list) == 10:
            break
    list.sort()
    print(list)
print(list)
addnum()
