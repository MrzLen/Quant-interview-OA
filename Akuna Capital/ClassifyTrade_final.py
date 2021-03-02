# Complete the function below.

import math
import operator
def classify(trades, labels, new_trades):
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

    def getResponse(neighbors,labwgt):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            votes=labwgt[response]
            if response in classVotes:
                classVotes[response] += votes
            else:
                classVotes[response] = votes
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    labs=set(labels)
    diclab={}
    labwgt={}
    for it in labs:
        diclab[it]=0
    for i in range(len(trades)):
        trades[i].append(labels[i])
        diclab[labels[i]]=diclab[labels[i]]+1
    labuq=list(diclab.keys())
    for l, ct in diclab.items():
        labwgt[l]=1.0/ct
    pred=[]
    for x in new_trades:
        neighbors=getNeighbors(trades,x,int(len(trades)**(0.5)))
        result=getResponse(neighbors,labwgt)
        pred.append(result)
    return(pred)

