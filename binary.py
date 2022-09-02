A=int(input())
binary=[]
ret=0
while(A>0):
    binary.append(A%2)
    A=int(A/2)
for i in reversed(range(0,len(binary))):
    ret=ret*10+binary[i]
print(ret)
