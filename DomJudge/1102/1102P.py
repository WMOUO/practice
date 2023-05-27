a = int(input())
n = [int(_) for _ in input().split(' ') if _]
ans = {0}
t = {0}
for i in n:
    r = set()
    for u in ans:r.add(u+i)
    ans = ans | r
ans = ans.difference(t)
print(len(ans))
for i in ans:print(i,end = ' ')