#arraySumExtraProblem
def solve(A,B):
    A=[0]+A
    B=[0]+B
    n=len(A)-1
    m=len(B)-1
    if m>n:
        A,B=B,A
        m,n=n,m
    s=0
    c=0
    while(m>=0):
        s=(A[n]+B[m]+c)%10
        c=(A[n]+B[m]+c)//10
        print(s,c)
        A[n]=s
        m=m-1
        n=n-1
    if c!=0:
        A[n]=A[n]+c
    if A[0]==0:
        A.pop(0)
    return A
A=[ 4, 3, 6, 7, 9, 9, 1, 7, 8 ]
B=[ 7, 5, 8, 9 ]
print(solve(A,B))