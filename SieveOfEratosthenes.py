n=int(input())
a=[]
a.append(0)
a.append(0)
for i in range(1,n):
    a.append(1)
p=2
while ((p*p)<=n):
    if a[p]==1:
        for i in range((p*p),n+1,p):
            a[i]=0
    p=p+1
ret=[]
for i in range(len(a)):
    if a[i]==1:
        ret.append(i)
print(ret)