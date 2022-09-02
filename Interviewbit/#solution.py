#Pickfrombothsides
def solve(A, B):
    sum=0
    for i in range(B):
        sum=sum+A[i]
    sumfinal=sum
    for i in range(B):
        sum=sum-A[B-i-1]+A[-1-i]
        if sum>sumfinal:
            sumfinal=sum
    return sumfinal
A=[5,4,-1,2,1]
print(solve(A,1))