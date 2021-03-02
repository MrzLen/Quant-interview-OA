market_share=[.4,.6]
switch_prob=[[.8,.2],[.1,.9]]
def matrixcal(arr, mat):
    res=[0]*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            res[i]=res[i]+arr[j]*mat[j][i]
    return res
res=matrixcal(market_share, switch_prob)
res_old=res
while (True):
    res=matrixcal(res,switch_prob)
    sum_t=sum([abs(res[i]-res_old[i]) for i in range(len(market_share)) ])
    res_old=res
    print(res)
    if sum_t<0.00001:
        break

print(res)
