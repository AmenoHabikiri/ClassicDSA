#ReorderDataInLogFiles
def myFunc(e):
    return e[1]
def rmDel(A):#func to remove delimeters
    n=len(A)
    dig=[]
    let=[]
    for i in range(n):
        B=list(map(str,A[i].split()))
        if B[1].isnumeric():
            dig.append(B)
        else:
            let.append(B)
    return let,dig
A = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
let,dig=rmDel(A)
let.sort(key=lambda x : x[1])
A=[]
for i in range(len(let)):
    A.append(" ".join(let[i]))
for j in range(len(dig)):
    A.append(" ".join(dig[j]))
print(A)
        

        