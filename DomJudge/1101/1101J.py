n = [int(_) for _ in input().split(' ') if _]
t = []
ans = 0
for i in range(len(n)):
    lol = 0
    if n[i] not in t:
        t.append(n[i])
    for u in range(i,len(n)):
        if n[i] == n[u]:
            lol += 1
    ans = max(ans,lol)
t.sort()
t.reverse()
t = list(map(str,t))
print(ans,' '.join(t))