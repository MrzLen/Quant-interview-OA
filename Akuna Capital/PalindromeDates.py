import datetime
a=2016
def checkdate(a, monthnum, daynum):
    try:
        newdate=datetime.datetime(int(a), int(monthnum), int(daynum))
        correctdate=True
    except ValueError:
        correctdate=False
    return correctdate

cen=a/100
sumdates=0
for i in range(1,101):
    # get each digit
    str_a=str(cen)+"{0:0=2d}".format(i)


    #check eight-digit
    monthnum=str_a[-1]+str_a[-2]
    daynum=str_a[-3]+str_a[-4]
    checkind=checkdate('2000', monthnum, daynum)

    if checkind==True:
        sumdates=sumdates+1
    #check seven-digit
    monthnum=str_a[-1]
    daynum=str_a[-2]+str_a[-3]
    checkind=checkdate('2000', monthnum, daynum)
    if checkind==True:
        sumdates=sumdates+1
print(sumdates)
