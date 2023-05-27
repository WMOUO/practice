a = int(input())
n = [int(_) for _ in input().split(' ') if _]
n.sort()
a = len(n)-1
ans = 0
for i in range(len(n),0,-1):
    ans += i * a
    a -= 1
print(ans)