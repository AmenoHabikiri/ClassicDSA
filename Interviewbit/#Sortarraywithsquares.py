#Sortarraywithsquares
def solve(A):
    li=[]
    li1=[]
    i=0
    k=0
    j=len(A)
    while (i<j):
        if(A[i]<=0):
            li=[A[i]**2]+li
            i=i+1
        else:
            
                
                
    return li   
A=[-9,-7,-6,-3,-1,0,1,2,3]
print(solve(A))
