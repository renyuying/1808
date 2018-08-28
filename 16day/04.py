def test(name):
    if name == '亚瑟':
        return '黑暗骑士'+name
    elif name  == '鲁班':
        return '电玩小子'+name
    elif name == '王昭君':
        return '爱情'+name
    else:
        print('不知道')
name = input('请输入英雄名字:')
ret = test(name)
print(ret)
