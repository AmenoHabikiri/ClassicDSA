#search in a special matrix
def binarySearch(A,k):
    start=0
    mid=0
    end=len(A)-1
    while(start<=end):
        mid=end+((start-end)//2)
        if A[mid]==k:
            return mid
        elif A[mid]<k:
            start=mid+1
        elif A[mid]>k:
            end=end-1
    return 0
def solve(A,B):
    k=binarySearch(A,k)
    while k
    