#moveZeroesToEnd
def moveZeroesToEnd(A):
    k=0
    n=len(A)
    while(k<n):
        if A[k]==0:
            A.pop(k)
            A.append(0)
            n=n-1
        else:
            k=k+1
    return A
A=[0,1,1,2,0,0,2,1,3,0,1]
print(moveZeroesToEnd(A))
        