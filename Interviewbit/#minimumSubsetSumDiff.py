#minimumSubsetSumDiff
import numpy as np
def solve(A):
    s=sum(A)//2
    n=len(A)
    dp=[[False for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j==0:
                dp[i][j]=True
            elif A[i-1]<=j:
                dp[i][j]=(dp[i-1][j] or dp[i-1][j-A[i-1]])
            else:
                dp[i][j]= dp[i-1][j]
    count=0
    for i in range(s+1):
        if dp[-1][i]==True:
            count=i    
    print(np.array(dp))
    return sum(A)-2*(count)
A=[1,1,1,11]
print(solve(A))
    