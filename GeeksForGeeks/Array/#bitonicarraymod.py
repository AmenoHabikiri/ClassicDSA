#bitonicarraymod
def binarySearch(A,k):
    n=len(A)
    beg=0
    end=n-1
    while beg<=end:
        mid=(beg+end)//2
        if A[mid]<k:
            beg=mid+1
        if A[mid]>k:
            end=mid-1
        if A[mid]==k:
            return mid
    return -1
def arrayRotate2(A,d):#O(d) 
    n=len(A)
    k=d%n
    for i in range(k):
        a=A[0]
        A.pop(0)
        A.append(a)
    return A 
def rotatedArrayBinarySearch(A,k):
    pivot=0
    for i in range(len(A)-1):
        if A[i]>A[i+1]:
            pivot=i
    if A[pivot]==k:
        return pivot
    elif A[0]>k :
        return (pivot+binarySearch(A[pivot:],k))
    else:
        return binarySearch(A[0:pivot],k)
A=list(map(int,input().split()))
k=int(input())
print(arrayRotate2(A,k))
f=int(input())
print(rotatedArrayBinarySearch(A,f))
