
def binarySearch(arr,beg,end,n):
    mid=(beg+end)//2
    if(arr[mid]>n):
        binarySearch(arr,beg,mid,n)
    else:
        if(arr[mid]<n):
            binarySearch(arr,mid,end,n)
        else:
            if(arr[mid]==n):
                return (mid+1)
            else:
                return 0
def search(arr,n):
    beg=0
    end=len(arr)
    return binarySearch(arr,beg,end,n)
arr=[1,3,5,7,100,192,1223,1300,2000,5000]
print(search(arr,192))

       