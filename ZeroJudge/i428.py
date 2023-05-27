z = []
mn = float('inf')
mx = 0
for _ in range(int(input())):
    z.append([int(_) for _ in input().split(' ') if _])
for i in range(1,len(z)):
    a = abs(z[i-1][0]-z[i][0]) + abs(z[i-1][1]-z[i][1])
    mn = min(a,mn)
    mx = max(a,mx)
print(mx,mn)