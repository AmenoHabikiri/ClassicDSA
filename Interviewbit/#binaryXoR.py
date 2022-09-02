def findMinXor(A):
    i=0
    ans=max(A)
    while(i<(len(A)-1)):
        j=i+1
        while(j<(len(A))):
            if i!=j:
                ans=min(ans,A[i]^A[j])
            j=j+1
        i=i+1
    return ans
def solve(A):
    A.sort()
    ans=A[1]-A[0]
    for i in range(1,len(A)):
        ans=min(ans,A[i]-A[i-1])
    return ans
A=[ 15, 5, 1, 10, 2 ]
print(findMinXor(A))