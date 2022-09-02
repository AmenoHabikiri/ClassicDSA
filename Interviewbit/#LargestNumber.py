#LargestNumber
def solve(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if int(str(A[i])+(str(A[j])))<int(str(A[j])+(str(A[i]))):
                A[i],A[j]=A[j],A[i]
    return A
A=[1,23,4,49,2]
print(solve(A))
        