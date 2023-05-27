z = ['True']*1000001
r = [0]*1000001
for i in range(2,1000001):
    if r[i] == 0:
        for u in range(i,1000001,i):
            if i == 2 or i == 3 or i == 5:
                z[u] = 'True'
            else:
                z[u] = 'False'
            r[u] = 1
a = int(input())
for i in [int(_) for _ in input().split(' ') if _]:
    print(z[i])