#choclates
import heapq
def solve(A,B):
    heapq._heapify_max(A)
    cout=0
    for i in range(B):
        cout=cout+A[0]
        A[0]=A[0]//2
        heapq._heapify_max(A)
        print(A)
    return cout
A=[ 2147483647, 2000000014, 2147483647 ]
print(solve(A,10))