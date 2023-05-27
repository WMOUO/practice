n = int(input())
m = [int(_) for _ in input().split(' ') if _]
for i in range(n-1) :
    for j in range(0,n-1):
        if m[j] > m[j+1] and m[j] % 2 == m[j+1] % 2:
            m[j],m[j+1] = m[j+1],m[j]
m = list(map(str,m))
print(''.join(m))