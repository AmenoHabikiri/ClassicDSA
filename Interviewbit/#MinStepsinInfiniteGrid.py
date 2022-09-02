#MinStepsinInfiniteGrid
def solve(A,B):
    k=0
    for i in range(len(A)-1):
        k=k+max(abs(A[i+1]-A[i]),abs(B[i+1]-B[i]))
    return k
A=[0,-1,2]
B=[0,-1,3]
print(solve(A,B))
        
