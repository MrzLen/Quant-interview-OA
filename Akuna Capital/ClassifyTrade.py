import math
import operator

trades=[[99.0,5.0,20.0],
        [95.0,15.0,10.0],
        [5.0,80.0,40.0],
        [3.0,92.0,20.0]]
labels=['green','green','red','red']
new_trades=[[90.0,10.0,15.0],
            [10.0,98.0,50.0]]
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors,minorlab,labwgt):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response==minorlab:
            votes=labwgt
        else:
            votes=1
        if response in classVotes:
            classVotes[response] += votes
        else:
            classVotes[response] = votes
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

labs=set(labels)
diclab={}
for it in labs:
    diclab[it]=0
for i in range(len(trades)):
    trades[i].append(labels[i])
    diclab[labels[i]]=diclab[labels[i]]+1
labuq=list(diclab.keys())
if diclab[labuq[0]]>diclab[labuq[1]]:
    minorlab=labuq[1]
    labwgt=1.0*diclab[labuq[0]]/diclab[labuq[1]]
else:
    minorlab=labuq[0]
    labwgt=1.0*diclab[labuq[1]]/diclab[labuq[0]]
pred=[]
for x in new_trades:
    neighbors=getNeighbors(trades,x,int(len(trades)**(0.5)))
    result=getResponse(neighbors,minorlab,labwgt)
    pred.append(result)
print(pred)
