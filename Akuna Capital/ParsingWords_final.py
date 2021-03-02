import sys
sq=[]
try:
    for line in sys.stdin:
        for it in line.strip().split(' '):
            sq.append(it)
except Exception:
    sq=''


dicwd={}
diclt={}
for i in range(ord('a'), ord('z')+1):
    diclt[chr(i)]=0
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
totalwords=sum([ct for keys, ct in dicwd.items()])
print(totalwords)
print('words')
for key in sorted(dicwd):
    print(key + ' ' + str(dicwd[key]))
print('letters')
for key in sorted(diclt):
    print(key + ' ' + str(diclt[key]))

