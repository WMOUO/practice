a = input()
b = input()
n = int(input())
z = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
for i in range(1,len(b)+1):
    for u in range(1,len(a)+1):
        if a[u-1] == b[i-1] :
            z[i][u] = z[i-1][u-1]+1
        else:
            z[i][u] = max(z[i-1][u],z[i][u-1])
if z[-1][-1] > n:
    print('kwa nini unaendesha')
else:
    print('sitini na tisa')