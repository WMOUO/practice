#累加
import bisect
a = int(input())
n = [int(_) for _ in input().split(' ') if _]
z = []
ans = set()
for i in range(len(n)):
    z.append([i])
r = 0
while len(z) != 0:
    p = []
    for i in range(len(z)):
        r = 0
        for t in z[i]:
            r += n[t]
        ans.add(r)
        for u in range(len(n)):
            if u not in z[i]:
                w = list(z[i])
                bisect.insort_right(w,u,lo=0,hi=len(w))
                if w not in p:
                    p.append(w)
    z = p
print(' '.join(map(str,sorted(list(ans)))))