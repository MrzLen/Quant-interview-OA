
def bisect_right(a,k,lo=0, hi=None):
    if lo<0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi=len(a)
    while lo<hi:
        mid=(lo+hi)//2
        if k==a[mid]: hi=lo=mid
        elif k<a[mid]: hi=mid
        else: lo=mid+1
    return lo

a=[1,3,5,6,7,10,22]
b=[]
k=7

ind=bisect_right(a,k)
if ind%2==0:
    medi=a[ind/2]
else:
    medi=(a[(ind+1)/2]+a[(ind-1)/2])/2
print(medi)
