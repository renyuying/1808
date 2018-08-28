def test(x,y,z,*args,a=100,**kwards):
    sum = 0
    sum+=x
    sum+=y
    sum+=z
    for i in args:
        sum+=i
    print(x)
    print(y)
    print(z)
    print(args)
    print(kwards)
    sum = 0
test(1,2,3,4,5,a=99,phon=2,age=13)
