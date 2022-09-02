def solve(n):
    k=1
    for i in range(1,n):
        k=k+2
    top=0
    bot=k
    left=0
    right=k
    dir=0
    li=[]
    for i in range(k):
        li.append([0 for i in range(k)])
    while n>0 and top<bot and left<right:
        if dir==0:
            for i in range(left,right):
                li[top][i]=n
            dir=1
            top=top+1
            continue
        if dir==1:
            for i in range(top,bot):
                li[i][right-1]=n
            dir=2
            right=right-1
            continue
        if dir==2: 
            for i in range(right,left-1,-1):
                li[bot-1][i]=n
            dir=3
            bot=bot-1
            continue
        if dir==3:
            for i in range(bot,top-1,-1):
                li[i][left]=n
            dir=0
            left=left+1
            n=n-1
        else: break
    for i in range(len(li)):
        print(li[i])
solve(9)
                        