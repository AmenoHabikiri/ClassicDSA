#rotatedSortedArray
def findMin(A):
    start=0
    end=len(A)-1
    mid=0
    if A[0]<A[1] and A[0]<A[-1]:
        return 0
    elif A[-1]<A[0] and A[-1]<A[-2]:
        return len(A)-1
    else:
        while(start<=end):
            mid=start+((end-start)//2)  
            if A[mid]<A[mid-1] and A[mid]<A[mid+1]:
                return mid
            elif A[mid]>A[0]:
                start=mid+1
            elif A[mid]<A[0]:
                end=mid-1
def binarySearch(A,start,end,k):
    mid=0
    while(start<=end):
        mid=start+((end-start)//2)
        if A[mid]==k:
            return mid
        elif A[mid]<k:
            start=mid+1
        elif A[mid]>k:
            end=mid-1
    return -1
def solve(A,k):
    minIndex=findMin(A)
    if A[minIndex]==k:
        return minIndex
    return max(binarySearch(A,0,minIndex-1,k),binarySearch(A,minIndex+1,(len(A)-1),k))
A=[4,5,6,7,8,1,2,3]
print(solve(A,3))
