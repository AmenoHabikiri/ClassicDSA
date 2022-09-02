#atoi
def solve(A):
    i=0
    while A[i]==" ":
        i=i+1
    s=""
    while i<len(A) and A[i] in ["1","2","3","4","5","6","7","8","9"]:
        s=s+A[i]
        i=i+1
    if s=="":
        return 0
    else:
        return int(s)
print(solve("87685"))