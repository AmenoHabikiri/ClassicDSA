#kthSmallestElement
def count(A,mid):
    cnt=0
    for i in range(len(A)):
        if A[i]<=mid:
            cnt=cnt+1
    return cnt
def solve(A,k):
    low=min(A)
    high=max(A)
    while(low<high):
        mid=low+(high-low)//2
        if count(A,mid)<k:
            low=mid+1
        else:
            high=mid
    return low
A=[7,3,4,1,5,3,2,6]
print(solve(A,4))