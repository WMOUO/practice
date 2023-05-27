w = 0
e = 0
r = {}
n = int(input())
m = [int(_) for _ in input().split(' ')if _]
for i in m:
    if r.get(i,"None") == "None":
        r[i] = 1
    else:
        r[i] += 1
for i in r.values():
    if i >= 10:
        w += 1
    if i >= 15:
        e += 1
print(f"{w} {e}")