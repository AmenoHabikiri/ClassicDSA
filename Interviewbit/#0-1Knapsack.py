#0-1Knapsack
def solve(A, B, C):#A: val B:weights
        dp=[[0 for i in range(C+1)] for j in range(len(A)+1)]
        for i in range(len(A)+1):
            for j  in range(C+1):
                if i==0 or j==0:
                    dp[i][j]==0
                elif B[i-1]<=j:
                    dp[i][j]=max((A[i-1]+dp[i-1][j-B[i-1]]),dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(A)][C]
A=[10,60,100]
B=[10,20,40]
C=100
print(solve(A,B,C))