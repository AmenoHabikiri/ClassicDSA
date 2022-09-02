def solve(A,k,i):
    if i==(len(A)): return -1
    if A[i]==k: return i
    else: return solve(A,k,i+1)
A=[2,5,6,7,7,9,11,2,3,7]
print(solve(A,7,0))