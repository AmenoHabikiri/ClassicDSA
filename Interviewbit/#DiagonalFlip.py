#DiagonalFlip
def solve(A):
    n=len(A)
    for i in range(n-1):
        for j in range(i,n):
            A[i][j],A[j][i]=A[j][i],A[i][j]
    return A
A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(solve(A))