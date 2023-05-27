z = []
for _ in range(int(input())):
    z.append([int(_) for _ in input().split(' ') if _])
z.sort(key=lambda x: -x[1])
r = 0
c = 0
for i in z:
    r += i[0]
    c = max(c-i[0], 0, i[1])
r += c
print(r)