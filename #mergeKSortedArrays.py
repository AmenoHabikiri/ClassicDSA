#mergeKSortedArrays
import heapq
A=[[1, 2, 3],[2, 4, 6],[0, 9, 10]]
k=list(heapq.merge(*A))
print(k)