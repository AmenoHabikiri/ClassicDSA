#allpossiblecombination
li=[]
def solve(s,idx,N):
    if idx==N:
        li2=s.copy()
        li.append(li2)
    else:
        for i in range(idx,N+1):
            s[idx],s[i]=s[i],s[idx]
            solve(s,idx+1,N)
            s[idx],s[i]=s[i],s[idx]
A=[1,2,3]
solve(A,0,len(A)-1) 
print(li)       
    