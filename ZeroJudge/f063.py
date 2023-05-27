ans = 0
for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    n = min(n[1:])
    ans = max(ans,n)
print(ans)