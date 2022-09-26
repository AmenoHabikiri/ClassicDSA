
def solve2(n,m,current):
    if m<n:
        return []
    if m==0:
        return [current]
    if n==0:
        return [current+m*")"]
    else:
        return solve2(n-1,m,current+"(")+solve2(n,m-1,current+")")
    
n=4    
s=""
li=[]
li=solve2(4,4,"")
print(li)

    
    