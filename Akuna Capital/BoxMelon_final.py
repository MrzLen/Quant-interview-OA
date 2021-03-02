# Complete the function below.


def  melon_count(boxes, melons):
    numbox=len(boxes)
    nummel=len(melons)
    maxsum=0
    for i in range(numbox):
        for mel in range(nummel):
            st=i
            currsum=0
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
        return maxsum

