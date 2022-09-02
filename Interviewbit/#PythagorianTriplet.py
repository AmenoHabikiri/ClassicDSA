#PythagorianTriplet
def solve(A):
    r=0
    for i in range(1,A):
        for j in range(1,A):
            s=(i*i+j*j)**(0.5)
            k=int(s)
            if (k==s) and s<=A:
                r=r+1
                print(i,j,s)
    return r//2
print(solve(13))
                
                