#subsetsumproblem
import numpy as np
def solve(A,i,n):
    if n==0:
        return True
    elif i<0:
        return False
    elif A[i]<=n: 
        return (solve(A,i-1,n-A[i]) or solve(A,i-1,n))
    elif A[i]>n:
        return solve(A,i-1,n)
def subsetSumDp(A,W,n):
    dp=[[False for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    print(np.array(dp))
    for i in range(1,n+1):
        for j in range(1,W+1):
            if A[i-1]<=j:
                dp[i][j]=(dp[i-1][j] or dp[i-1][j-A[i-1]])
            elif A[i-1]>j:
                dp[i][j]=(dp[i-1][j])
    return dp[-1][-1]
A=[1,3,5,9,6,2]
print(subsetSumDp(A,14,len(A)))