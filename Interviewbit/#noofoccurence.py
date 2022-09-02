def binarySearch(A,k):
    mid=0
    start=0
    end=len(A)-1
    while(start<=end):
        i=-1
        j=-1
        mid=start+((end-start)//2)
        if A[mid]==k:
            return mid               
        elif A[mid]<k:
            start=mid+1
        elif A[mid]>k:
            end=mid-1
    return -1
def Solve(A,k):
    if A[0]==A[-1] and A[0]==k:
        return len(A)
    ind=binarySearch(A,k)
    i=ind
    j=ind
    if ind==-1:
        return 0
    else:
        while A[i-1]==A[ind]:
            i=i-1
        while A[j+1]==A[ind]:
            j=j+1
        return j-i+1
A=[1]
print(Solve(A,2))