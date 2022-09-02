#Smaller or equal elements
def binarySearch(A, B):
    if A[-1]<B:
        return len(A)
    else:
        mid=0
        start=0
        end=len(A)-1
        while(start<=end):
            mid=start+((end-start)//2)
            if A[mid]==B:
                return mid
            elif mid>0 and A[mid-1]<B and A[mid]>B:
                return mid-1
            elif A[mid]>B:
                end=mid-1
            elif A[mid]<B:
                start=mid+1
A=[x for x in range(1000)]
print(binarySearch(A,152))
