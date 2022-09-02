#RearrangeArray
def solve(A):
    k=[]
    for i in range(len(A)):
        k.append(A[A[i]])
    print(k)
    return A

A=[1,2,3 4,5]
print(solve(A))   