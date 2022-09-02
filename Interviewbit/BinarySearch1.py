#binarySearchNormal
def solve1P(A,k):
    start=0
    end=len(A)-1
    res=-1
    mid=0
    while(start<=end):
        mid= start + (end-start)//2
        if A[mid]==k:
            return mid
        elif A[mid]>k:
            end=mid-1
        else:
            start=mid+1
    return -1
A=[1,2]
print(solve1P(A,2))
        
    
    