#uniqueSubsets
def solve(inp,out,li):
    if len(inp)==0:
        li.append(",".join(out))
        return 
    solve(inp[1:],out,li)
    solve(inp[1:],out+[inp[0]],li)
inp=[1,2,3,1]
for i in range(len(inp)):
    inp[i]=str(inp[i])
li=[]
solve(inp,[],li)
li=list(set(li))
k=[]
for i in range(len(li)):
    if li[i]=='':
        k.append([])
    else:
        k.append(list(map(int,li[i].split(','))))
print(k)

    
