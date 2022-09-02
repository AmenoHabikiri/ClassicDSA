#MaximumAbsoluteDifference
def solve(A):
    total=0
    a=len(A)
    li1=[]
    li2=[]
    for i in range(a):
        li1.append(A[i]+i)
        li2.append(A[i]-i)
    total=max((max(li1)-min(li1)),(max(li2)-min(li2)))
    return total
A=[1, 3, -1]
print(solve(A))            