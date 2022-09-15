#countSubset
def solve(A,n,W):
    dp=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if j==0:
                dp[i][j]=1
            elif A[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-A[i-1]]
            elif A[i-1]>j:
                dp[i][j]=dp[i-1][j]
    return dp[n][W]
A=[1,1,1,1,1]
print(solve(A,len(A),4))