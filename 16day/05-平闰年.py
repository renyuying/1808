def calu():
    days = 0
    date = '20180827'
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:])
    big_month = [1,3,5,7,8,10,12]
    small_month = [4,6,9,11]
    for i in range(1,month):
        if i in big_month:
            days+=31
        elif i in small_month:
            days+=30
        else:
            if check(year)
                days+=28
    days+=day
    print(days)
def checkyear(year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return  True
        else:
            return　False
calu()
