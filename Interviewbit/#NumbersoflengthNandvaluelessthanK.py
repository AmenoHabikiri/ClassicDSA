#NumbersoflengthNandvaluelessthanK
def lesser(A,n):
    k=0
    for i in range(len(A)): 
        if A[i]<=n:k=k+1
    return k
def lesser2(A,li):
    k=1
    n=0
    for i in range(1,len(li)):
        n=lesser(A,li[i])
        k=k*n
    return k
def solve(A,B,C):
    if len(A)==0:
        return 0
    c=str(C)
    li=[]
    for i in c: li.append(int(i))
    c=len(li)
    a=len(A)
    if B>c: return 0
    elif B<c or li[0]>A[-1]:
        if A[0]==0: return ((a**(B-1))*(a-1))
        else: return (a**B) 
    elif B==c:
        k=[]
        x=lesser(A,li[0])-1
        if A[0]==0: x=x-1
        x=x*(a**(c-1))
        x=x+lesser2(A,li)-1
        return x 
A=[0]
B=3
C=1000
print(solve(A,B,C))