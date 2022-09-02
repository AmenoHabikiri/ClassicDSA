#findDuplicateInArray
def solve(A): #
    for i in range(len(A)):
        if A[abs(A[i])] <0:
            return (A[i]*-1)
        else:
            A[abs(A[i])]*=-1
    return -1
A=[4,2,5,1,3,2]
print(solve(A))
    