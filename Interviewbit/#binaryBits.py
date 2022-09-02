def solve(m):
    b=""
    while m>=1:
        b=b+str(m%2)
        m=m//2
    k=0
    for i in b:
        if i=="1":
            k=k+1
    return b   
print(solve(1))
        