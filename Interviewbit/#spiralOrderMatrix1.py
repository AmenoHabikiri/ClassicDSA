#spiralOrderMatrix1
def spiralOrderMatrix(A):
    sr=0
    er=len(A)-1
    sc=0
    ec=len(A[0])-1
    k=[]
    l=len(A)*len(A[0])
    x=0
    while (sr<=er and sc<=ec and x<l):
        if sc<=ec and x<l:
            for i in range(sc,ec+1):
                k.append(A[sr][i])
                x+=1
            sr=sr+1
        if sr<=er and x<l:
            for i in range(sr,er+1):
                k.append(A[i][ec])
                x+=1
            ec=ec-1
        if sc<=ec and x<l:
            for i in reversed(range(sc,ec+1)):
                k.append(A[er][i])
                x+=1
            er=er-1
        if sr<=er and x<l:
            for i in reversed(range(sr,er+1)):
                k.append(A[i][sc])
                x+=1
            sc=sc+1
    return k
A=[]
n=int(input())
for i in range(n):
    k=list(map(int,input().split()))
    A.append(k)
for i in range(len(A)):
    print(A[i])
print(spiralOrderMatrix(A))       
    