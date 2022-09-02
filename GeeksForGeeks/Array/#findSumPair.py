#findSumPair
def arrayRotate2(A,d):#O(d) 
    n=len(A)
    k=d%n
    for i in range(k):
        a=A[0]
        A.pop(0)
        A.append(a)
    return A 
def findSumPair(arr,x): 
    pivot=-1
    n=len(arr)
    for i in range(0, n - 1):
        if (arr[i] > arr[i + 1]):
            pivot=i
             
    # l is now index of smallest element       
    l = (pivot + 1) % n
    # r is now index of largest element
    r = pivot   
    while (l != r):
        if ((arr[l] + arr[r]) == x):
            print(arr[l],arr[r])
        if ((arr[l] + arr[r]) < x):
            l = (l + 1) % n
        else:
            r = ( n+r - 1) % n
    
A=list(map(int,input().split()))
x=int(input())
k=int(input())
arrayRotate2(A,x)
print(A)
findSumPair(A,k)