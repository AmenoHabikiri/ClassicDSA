#vowelAndConsonant
v=0
c=0
A="ababaab"
for i in A:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        v=v+1
    else:
        c=c+1
print(v*c)