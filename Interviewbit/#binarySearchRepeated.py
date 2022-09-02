#binarySearchRepeated
def solve1P(A,k):
    start=0
    end=len(A)-1
    res=-1
    mid=0
    while(start<=end):
        mid=start+(end-start)//2
        if A[mid]==k:
            res=mid
            end=mid-1
        elif A[mid]>k:
            end=mid-1
        else:
            start=mid+1
    return res
def solve1E(A,k):
    start=0
    end=len(A)-1
    res=-1
    mid=0
    while(start<=end):
        mid=start+(end-start)//2
        if A[mid]==k:
            res=mid
            start=mid+1
        elif A[mid]>k:
            end=mid-1
        else:
            start=mid+1
    return res
def solve(A,k):
    p=solve1P(A,k)
    e=solve1E(A,k)
    return (p,e)
A=[1,2,2,2,3,4,5,6]
print(solve(A,2))
        
    
    
    