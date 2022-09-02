#segregate0and1
def solve(self, A):
    k=len(A)
    j=0
    while j<k:
        if A[j]==1:
            A.pop(j)
            A.append(1)
            k=k-1
        else:
            j=j+1
    return A