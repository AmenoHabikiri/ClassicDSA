def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if (arr[j]>arr[j+1]):
                c=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=c
    return arr
array=[10,9,8,11,16,5,4,13,2,1,10]
print(bubble(array))
            