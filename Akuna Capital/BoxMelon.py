boxes=[3,2,1,5,6,3]
melons=[2,1,3,4,9]

numbox=len(boxes)
nummel=len(melons)
maxsum=0
for i in range(numbox):
    st=i
    currsum=0
    mel=0
    while (True):
        if boxes[st]>=melons[mel]:
            currsum=currsum+1
            mel=mel+1
        st=st+1
        if st==numbox or mel==nummel:
            break
    maxsum=max(maxsum,currsum)
    if maxsum==nummel:
        break
print(maxsum)


