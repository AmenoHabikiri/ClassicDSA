#insertelementinsortedarraybyrecursion
def insertElement(A,n,val):
    if n==0:
        k=[val]+A 
        return k
    else:
        if A[n-1]<=val:
            k=A[0:n]+[val]+A[n:len(A)]
            return k
        else:
            return insertElement(A,n-1,val)
A=[1,2,7,8,11,14]
print(insertElement(A,len(A),0))


        