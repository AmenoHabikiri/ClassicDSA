def solve(A,i,k,n):
    if i==len(A):
        return n
    if A[i]==k:
        n.append(i)
    return solve(A,i+1,k,n)
A=[]
def findindex(A,k):
    n=solve(A,0,k,[])
    if n==[]:
        n=-1
    print(n)
A=[2]
findindex(A,1)