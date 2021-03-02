for line in sys.stdin:
        print line

sq=['im','good', 'andyou','d*ji','go99','*']
dicwd={}
diclt={}

for i in range(len(sq)):
    wd=sq[i]
    notwd=0
    for l in wd:
        if ord(l)<97 or ord(l)>122:
            notwd=1
            break
    if notwd==0:
        for l in wd:
            if l not in diclt:
                diclt[l]=1
            else:
                diclt[l]=diclt[l]+1
        if wd not in dicwd:
            dicwd[wd]=1
        else:
            dicwd[wd]=dicwd[wd]+1
print(len(dicwd))
if 'words' in dicwd:
    print(dicwd['words'])
else:
    print(0)
for key in sorted(dicwd):
    print(key + ' ' + str(dicwd[key]))

if 'letters' in dicwd:
    print(dicwd['letters'])
else:
    print(0)

for key in sorted(diclt):
    print(key + ' ' + str(diclt[key]))
