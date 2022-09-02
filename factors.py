N=int(input())
ret=[]
i=1
prime=[]
prime.append(0)
prime.append(0)
for i in range(1,N):
    prime.append(1)
p=2
while(p*p<=N):
    if prime[p]==1:
        for i in range(p*p,N+1,p):
            prime[i]=0
    p=p+1
for i in range(len(prime)):
    if prime[i]==1:
        if N%i==0:
            ret.append(i)
ret1=[0 for i in range(len(ret))]
for i in range(0,len(ret1)):
    k=ret[i]
    while(N%k==0):
        ret1[i]+=1
        k=k*k
print(ret)
print(ret1)

    

    