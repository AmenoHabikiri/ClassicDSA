#kthPermutation
def factorial(k):
    n=1
    i=1
    while(n<k):
        n=n*i
        i+=1
    return n//(i-1),(i-2)
def solve(A,B):
    li=[]
    li1=[]
    li3=[]
    for i in range(1,A+1):
        li.append(i)
    if B==1:
        return li
    else:
        B=B-1
        A=A-1
        k,i=factorial(B)
        while(B>=0 and i>0):
            li1.append(B//k)
            B=B%k
            k=k//i
            i=i-1
        li1.append(0)
        for i in range(A,len(li1)-1,-1):
            li1=[0]+li1
        print(li1)
        for i in range(len(li1)):
            li3.append(li[li1[i]])
            li.pop(li1[i])        
    return li3
print(solve(5,25))
