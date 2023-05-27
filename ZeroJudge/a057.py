n = int(input())
z = [1]
i = 0
while len(z) < n*3:
    if z[i]*2 not in z:z.append(z[i]*2)
    if z[i]*3 not in z:z.append(z[i]*3)
    if z[i]*5 not in z:z.append(z[i]*5)
    i += 1
    z.sort()
print(z[n-1])