#SubsetDifference
def solve(A,n,diff):
    W=(diff+sum(A))//2
    dp=[[0 for i in range(W+1)] for i in range(n+1)]
    for i in range(W+1):
        for j in range(n+1):
            if j==0:
                dp[i][j]=1
            elif A[i-1]<=j:
                dp[i][j]=dp[i-1][j-A[j-1]]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return (dp[-1][-1]+1)//2
A=[1,1,2,3]
print(solve(A,len(A),1))     