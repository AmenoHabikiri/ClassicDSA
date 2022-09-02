#minimumParanthesis
def solve(A):
    count=0
    ans=0
    for i in A:
        if i=="(":
            count=count+1
        elif i==")":
            count=count-1
        if count<0:
            ans=ans+1
            count=0
    ans=count+ans
    return ans
A=input()
print(solve(A))