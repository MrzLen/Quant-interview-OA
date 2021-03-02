a=['1234-1','1235-1','1236-5','1235-3','1234-2']
drone=[]
droneseq=[]
homedic={}
timedic={}
lasttimedic={}
for it in a:
    pos=it.find('-')
    dr=it[:pos]
    hs=it[pos+1:]
    droneseq.append(dr)
    if dr not in drone:
        drone.append(dr)
        homedic[dr]=[int(hs)]
        timedic[dr]=[0]
        lasttimedic[dr]=0
    else:
        homedic[dr].append(int(hs))
        timedic[dr].append(0)
for dr, hn in homedic.items():
    for i in range(len(hn)):
        if i==0:
            timedic[dr][i]=hn[i]
        else:
            timedic[dr][i]=hn[i]-hn[i-1]+1
timesum=0
for dr in droneseq:
    if timesum==0:
        t=timedic[dr].pop(0)
        timesum=t
    else:
        t=timedic[dr].pop(0)
        timesum=max(timesum+(t-(timesum-lasttimedic[dr])),timesum+1)
    lasttimedic[dr]=timesum
print(timesum)
