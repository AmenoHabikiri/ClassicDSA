#MakeEqualElementsArray
def solution(A,B):
    k=list(set(A))
    n=len(k)
    print(n)
    if n>3:
        return 0
    elif n==3:
        if (k[1]-k[0])==B and (k[2]-k[1])==B:
            return 1
        else: return 0
    elif n==2:
        if (k[1]-k[0])==B:
            return 1
        else:
            return 0
    else:
        return 1
A=[ 3, 1, 2, 1, 3, 1, 2, 2, 1, 1, 2, 3, 3, 1, 3, 3, 3, 2, 3, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3, 3, 1, 1, 3, 2, 2, 3, 1, 2, 1, 3, 3, 3, 2, 1, 1, 2, 1 ]
print(solution(A,1))