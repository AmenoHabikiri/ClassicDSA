#RearrangeArray
def solve(A):
    k=[]
    N=len(A)
    for i in range(N):
        A[i]=A[i]+(A[A[i]]%N)*N
    for i in range(N):
        A[i]=A[i]//N
    return A
A=[5,4,3,2,1,0]
print(A)
print(solve(A))   