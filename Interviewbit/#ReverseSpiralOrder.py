#ReverseSpiralOrder
def solve(A,r,c):
    lis=[]
    for i in range(r):
        lis.append([0]*c)
    top=0
    bot=len(lis)-1
    left=0
    right=len(lis[0])-1
    k=0
    dir=0
    print(lis)
    while (top<=bot) and (left<=right) and k<len(A):
        if left<=right and k<len(A):
            for i in range(left,right+1):
                lis[top][i]=A[k]
                k=k+1
            top=top+1
        if top<=bot and k<len(A):
            for i in range(top,bot+1):
                lis[i][right]=A[k]
                k=k+1
            right=right-1
        if left<=right and k<len(A):
            for i in range(right,left-1,-1):
                lis[bot][i]=A[k]
                k=k+1
            bot=bot-1
        if top<=bot and k<len(A):
            for i in reversed(range(top,bot+1)):
                lis[i][left]=A[k]
                k=k+1
            left=left+1
    print(lis)
                
A=[1,2,3,4,5,6,7,8,9,10,11,12]
solve(A,3,4)
    