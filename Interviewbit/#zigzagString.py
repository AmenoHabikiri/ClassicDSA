#zigzagString
def solve(A,B):
    li=[]
    for i in range(B):
        li.append([])
    print(li)
    up=0
    down=1
    k=0
    for j in A:
        print(k)
        li[k].append(j)
        if down==1 and k<(B-1):
            k=k+1
        elif k==(B-1):
            up=1
            down=0
            k=k-1
        elif up==1 and k>0:
            k=k-1
        elif k==0:
            up=0    
            down=1
            k=k+1
    s=""
    for i in range(len(li)):
        for j in range(len(li[i])):
            s=s+li[i][j]
    return s
print(solve("paypalishiring",3))
    