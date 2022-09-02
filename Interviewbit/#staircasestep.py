#staircasestep
def steps(curr,n,li):
    if n<curr: 
        return
    li.append(curr)
    if n==curr:
        print(li)
        li.pop()
        return 
    steps(curr+1,n,li)
    steps(curr+2,n,li)
    li.pop()
steps(1,10,[])
    