#arrayRotation1
def arrayRotate(A,d,n):
    li=[]
    d=d%n
    for i in range(d):
        li.append(A[i])
        A.append(li[i])
    for i in range(d):
        A.pop(0)
    print(li)
    return A
def arrayRotate1(L,d,n):
    k=d%n
    lis=[]
    lis=L[k:]+L[0:k]
    print(lis)
def arrayRotate2(A,d,n):#O(d)
    k=d%n
    for i in range(k):
        a=A[0]
        A.pop(0)
        A.append(a)
    return A 
def swap(arr,fi,si,d):
    for i in range(d):
        temp=arr[fi+i]
        arr[fi+i]=arr[si+i] 
        arr[si+i]=temp
def BlockSwap(A,d,n):
    if (d==0 or d==n):
        return
    i=d
    j=n-d
    while (i!=j):
        if (i<j):
            swap(A,d-i,d+j-i,i)
            j=j-i
        else:
            swap(A,d-i,d,j)
            i=i-j
    swap(A,d-i,d,i)
    return
A=list(map(int,input().split()))
k=int(input())
#print(arrayRotate2(A,k,len(A)))
BlockSwap(A,k,len(A))
print(A)