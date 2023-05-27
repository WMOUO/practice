n = int(input())
m = [int(_) for _ in input().split(" ") if _]
m.sort()
ans = ''
for i in m:
    i = str(i)
    ans += i
print(ans)