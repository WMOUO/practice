a = int(input())
n = [int(_) for _ in input().split(" ") if _]
h = 1
j = 0
z = []
while h < a:
    if j + h >= a:
        k = j+h-a
        g = sum(n[j:])+sum(n[:k])
        if g not in z:z.append(g)
    else:
        if sum(n[j:j+h]) not in z:z.append(sum(n[j:j+h]))
    j += 1
    if j == a:
        j = 0
        h += 1
z.append(sum(n))
print(len(z))
z.sort()
z = map(str,z)
print(" ".join(z))