#phonedigits
dict={1:'abc',2:'def',3:'ghi',4:'jkl',5:'mno',6:'pqrs',7:'tuv',8:'wxyz'}
def solve(dict,n,li,curr):
    if len(n)==curr:
        print(li)
        return 
    for i in range(len(dict[n[curr]])):
        li.append(dict[n[curr]][i])
        solve(dict,n,li,curr+1)
        li.pop()
        if (n[curr]==0 ):
            return
n=[1,2,3]
print(dict[1])
solve(dict,n,[],0)
