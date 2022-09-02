def solve(k):
    low=1
    high=k
    ans=0
    while(low<=high):
        mid=(high+low)//2
        sqr=mid*mid
        if sqr==k:
            return mid
        if sqr>k:
            high=mid-1
        if sqr<k:
            ans=mid
            low=mid+1
    return ans
print(solve(0))
            
            