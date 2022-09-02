#stepsinamaze
def solve(i,j,n,li):
    if n<i and n<j:
        return
    li.append([i,j]) 
    if n==i and n==j:
        print(li)
        li.pop()
        return 
    if n>i and n>j:
        solve(i+1,j,n,li)
        solve(i,j+1,n,li)
        li.pop()
    elif n==i :
        solve(i,j+1,n,li)
        li.pop()
    elif n==j :
        solve(i+1,j,n,li)
        li.pop()
solve(1,1,2,[])