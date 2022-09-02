#maxSumOnlyRotation
def arrayRotate2(A,d):#O(d) 
    n=len(A)
    k=d%n
    for i in range(k):
        a=A[0]
        A.pop(0)
        A.append(a)
    return A
def maxSumOnlyRotation(A):
    sum1=0
    li=A
    k=0
    n=len(A)
    for i in range(n):
        sum1=sum1+i*A[i]
        k=k+A[i]
    sum=sum1
    pivot=-1
    for i in range(1,n): 
        sum1=sum1-A[n-i]*(n)+k
        if sum1>sum:
            sum=sum1
            pivot=i
    return arrayRotate2(A,n-pivot)
A=list(map(int,input().split()))
print(maxSumOnlyRotation(A))