#selltickets
#heap_sort
def heapify(A,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and A[i]>A[l]:
        largest=l
    if r<n and A[largest]>A[r]:
        largest=r
    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        heapify(A,n,largest)    
def heapSort(A):
    n=len(A)
    for i in range(n//2-1,-1,-1):
        heapify(A,n,i)
    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)
def solve(A,B):
    n=len(A)
    heapSort(A)
    cout=0
    for i in range(B):
        cout=cout+A[0]
        A[0]=A[0]-1
        j=0
        k=1
        while A[j]<A[k]:
            A[j],A[k]=A[k],A[j]
            j=j+1
            k=k+1
        print(A,cout)
    return cout
                    
A=[13,12,11,5,6,7]
solve(A,4)

    
    