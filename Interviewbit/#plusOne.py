#plusOne
def plusOne(A):
        if A[0]!=0:
            A=[0]+A
        s=0
        c=1
        for i in range((len(A)-1),-1,-1):
            s=(c+A[i])
            c=s//10
            s=s%10
            A[i]=s
        while (A[0]==0):
            A.pop(0)
        return A
A=[0]
print(plusOne(A))