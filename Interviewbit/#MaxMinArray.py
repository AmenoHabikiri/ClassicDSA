#MinHeapSort
def swap(A,i,j):
    A[i],A[j]=A[j],A[i]
def heapify(A,i,upper):
    while(True):
        l,r=i*2+1,i*2+2
        if max(l,r)<upper:
            if A[i]<=min(A[l],A[r]): break
            elif A[l]<A[r]:
                    swap(A,i,l)
                    i=l
            elif A[r]<A[l]:
                    swap(A,i,r)
                    i=r
        elif r<upper:
            if A[r]<A[i]:
                swap(A,i,r)
                i=r
            else:
                break
        elif l<upper:
            if A[l]<A[i]:
                swap(A,i,l)
                i=l
            else:
                break
        else:
            break
def heapsort(A):
    for i in range((len(A)-2)//2,-1,-1):
        heapify(A,i,len(A))
    for end in range(len(A)-1,0,-1):
        swap(A,0,end)
        heapify(A,0,end)
lis=[5,16,8,14,20,1,26]
heapsort(lis)
sum=lis[0]+lis[-1]
print(sum)