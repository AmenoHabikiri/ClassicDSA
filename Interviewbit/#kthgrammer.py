#kthgrammer
import sys
sys.setrecursionlimit(10**6)
def solve(n,k):
    if n==1 and k==1:
        return 0
    mid=2**(n-1)
    if k<=mid:
        return solve(n-1,k)
    else:
        return ( not solve(n-1,k-mid))
print(solve(3,4))            
        
    