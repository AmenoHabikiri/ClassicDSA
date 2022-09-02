#SetIntersection
def solve(A):
    A.sort()
    li=[A[0][-1]-1,A[0][-1]]
    k=len(A)
    #exception
    for i in range(1,k):
        if A[i][0]>li[-1]:
            li.append(A[i][0])
            li.append(A[i][0]+1)
        elif A[i][0]==li[-1]:
            li.append(A[i][0]+1)
        elif A[i][-1]<li[0]:
            li=[A[i][-1]]+li
            li=[A[i][-1]-1]+li
        elif A[i][-1]==li[0]:
            li=[A[i][-1]-1]+li
    return li
A = [[1, 2], [4,9], [8, 9]]
A2=[[1, 2], [2, 3], [2, 4], [4, 5]]
print(solve(A))
