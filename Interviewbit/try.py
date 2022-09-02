def solve(A,B):
    k=[]
    for i in A: 
        k.append(i)
    l=int(k[-1])
    cycle=0
    if (l==1) or (l==0) or (l==5) or (l==6):
        cycle=1
    elif (l==2 or l==3 or l==7 or l==8):
        cycle=4
    elif (l==4 or l==9):
        cycle=2
    n=int(B)%cycle
    if n==0 or n==1:return l
    else:
        n=n+1
        if l==4 :return 6
        if l==9 :return 1
        if n==1:
            if l==2 or l==8: return 4
            if l==3 or l==7: return 9
        if n==2:
            if l==2: return 4
            if l==3: return 7
            if l==7: return 3
            if l==8: return 2
        if n==3:
            if l==8 or l==2: return 6
            if l==3 or l==7: return 1
        
         
print(solve("117","2"))
        
        
    