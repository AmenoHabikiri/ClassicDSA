A=int(input())
factors = []
for i in range(1, int(A**0.5) + 1):
    if A%i == 0:
        factors.append(i)
        if i != A**0.5:
            factors.append(int(A/i))
factors.sort()
print(factors)