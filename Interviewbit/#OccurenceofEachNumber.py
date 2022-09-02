#OccurenceofEachNumber
def solve(A):
    A.sort()
    s=A[0]
    k=1
    num=[]
    for i in range(1,len(A)):
        if A[i]==s:
            k+=1
        else:
            num.append(k)
            s=A[i]
            k=1
    num.append(k)
    return num
A=[ 1, 2, 3, 2, 2, 1, 2, 2, 2, 1 ]
A.sort()
print(A)
print(solve(A))