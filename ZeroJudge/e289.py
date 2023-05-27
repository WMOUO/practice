a = [int(_) for _ in input().split(' ') if _]
n = [int(_) for _ in input().split(' ') if _]
z = {}
r = 0
ans = 0
for i in range(len(n)):
    if i >= a[0]:
        z[n[i-a[0]]] -= 1
        if z[n[i-a[0]]] == 0:
            r -= 1
    if z.get(n[i],None) != None :
        z[n[i]] += 1
        if z[n[i]] == 1 :
            r += 1
    else:
        z[n[i]] = 1
        r += 1
    if r == a[0]:
        ans += 1
print(ans)
#3 9
#1 2 3 3 3 5 4 3 1 2