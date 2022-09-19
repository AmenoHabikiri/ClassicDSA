#unboundedKnapsack
import numpy as np
def solve(Val,wt,W):
    n=len(Val)
    dp=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if wt[i-1]<=j:
                dp[i][j]=max((Val[i-1]+dp[i][j-wt[i-1]]),dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    print(np.array(dp))
    return dp[-1][-1]
V=[1, 4, 5, 7]
wt=[1, 3, 4, 5]
print(solve(V,wt,8))