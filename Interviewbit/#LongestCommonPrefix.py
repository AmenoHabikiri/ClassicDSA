#LongestCommonPrefix
def common(k,l):
    str=""
    i=0
    x=min(len(k),len(l))
    while i<x and k[i]==l[i]:
        str=str+k[i]
        i=i+1
    return str
def solve(A):
    if A==[] or "" in A:
        return ""
    pref=A[0]
    for i in range(1,len(A)):
        pref=common(pref,A[i])
    return pref  
A=["abcdef","abdef","abccdde","abc","abcddd"]
solve(A)