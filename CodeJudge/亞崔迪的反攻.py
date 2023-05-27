r = int(input())
n = sorted([int(_) for _ in input().split(' ') if _])
for i in range(len(n)):
    r = min(r,n[i]+len(n)-(i+1))
print(r)