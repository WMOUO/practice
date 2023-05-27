a = int(input())
n = [int(_) for _ in input().split(' ') if _]
r = 1
ans = 0
for i in n:
    ans += i*r
    r += 1
print(ans)