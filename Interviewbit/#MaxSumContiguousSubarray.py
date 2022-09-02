#MaxSumContiguousSubarray
def maxArray(A,n):
    sum=0
    for i in range(n):
        sum=sum+A[i]
    sumfinal=sum
    for j in range(n,len(A)):
        sum=sum+A[j]-A[j-n]
        if sum>sumfinal:
            sumfinal=sum
    return sumfinal
def solve(A):
    total=maxArray(A,1)
    for i in range(1,len(A)+1):
        sum=maxArray(A,i)
        if sum>total:
            total=sum
    return total
A=[-500,501]
print(solve(A))
        

    
        

