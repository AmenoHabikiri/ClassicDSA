#heapSort
def swap(A,i,j):
    A[i],A[j]=A[j],A[i]
def heapify(lis,i,upper):
    while(True):
        left=i*2+1
        right=i*2+2
        if max(left,right)<upper:
            if lis[i]>=max(lis[left],lis[right]):
                break
            elif lis[left]>lis[right]:
                swap(lis,i,left)
                i=left
            else:
                swap(lis,i,right)
                i=right
        elif left<upper:
            if lis[left]>lis[i]:
                swap(lis,i,left)
                i=left
            else:
                break
        elif right<upper:
            if lis[right]>lis[i]:
                swap(lis,i,right)
                i=right
            else: 
                break
        else:
            break
def heapsort(lis):
    for j in range((len(lis)-2)//2,-1,-1):
        heapify(lis,j,len(lis))
    for end in range(len(lis)-1,0,-1):
        swap(lis,0,end)
        heapify(lis,0,end)
lis=[5,16,8,14,20,1,26]
heapsort(lis)
print(lis)
    