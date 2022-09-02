#positiveNegative
def solve(A):       
    p=0
    n=0
    for i in range(len(A)):
        if A[i]<0:
            n=n+1
        if A[i]>0:
            p=p+1
    k=[]
    k.append(p)
    k.append(n)
    return k
A=[-1,0,1]
print(solve(A))