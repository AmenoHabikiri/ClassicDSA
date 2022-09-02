#numberOfRotation
def minBinarySearch(A):
    beg=0
    end=len(A)-1
    while(beg<end):
        mid=(beg+end)//2
        if A[mid-1]>A[mid]:
            return mid
        if A[mid]>A[mid+1]:
            

                
        